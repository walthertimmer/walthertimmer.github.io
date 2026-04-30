---
title: databricks app met serverless lakebase connectie opzetten
date: 2026-04-30
description: een databricks app en samenhangende instellingen volledig via API uitrollen
---

# databricks app met serverless lakebase connectie opzetten

Het is altijd mooi als er nieuwe technische dingen mogelijk zijn zoals nu Databricks die haar laatste aanschaf van serverless PostgreSQL (oftewel het bedrijf Neon) verder integreert in het databricks aanbod onder noemer van lakebase. 
Waar eerder provisioned PostgreSQL databases mogelijk waren is het nu verplicht om elke nieuwe PostgreSQL database als “auto provisioned serverless lakebase” database to te voegen. 

Het jammere daarbij is alleen dat terwijl dit direct live gezet is  de oudere provisioned variant niet meer neergezet kan worden voor nieuwe databases en daarmee werkende CI/CD pipelines voor nieuwe projecten niet meer gehanteerd kunnen worden. 
Gelukkig blijven bestaande projecten wel intact. Echter loop je dan tegen het volgende punt aan dat zowel Databricks Bundles als ook CLI nog niet volledig de nieuwe syntax voor alle stappen ondersteunen en je dus voor een aantal stappen van de Databricks API afhankelijk bent waarvoor de requests en APIs nog niet volledig beschreven zijn aangezien alles nog preview of beta is. 

Dus wil je een nieuwe stijl Databricks app inclusief metrics, inclusief serverless Lakebase connectie, inclusief rechten neerzetten moet je een aantal stappen uitvoeren; namelijk:

1. maak lakebase project aan (je krijgt er automatisch een default endpoint en branch bij)

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/postgres/projects?project_id=${{ parameters.databricksAppsName }} --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/database.json"
```
met als payload:

```json
{
  "spec": {
    "display_name": "${databricksAppsName}",
    "budget_policy_id": "${budgetPolicyId}",
    "custom_tags": {
      "cpt_service": "postgresql"
    },
    "pg_version": 17,
    "history_retention_duration": "172800s",
    "default_endpoint_settings": {
      "autoscaling_limit_max_cu": 0.5,
      "autoscaling_limit_min_cu": 0.5,
      "suspend_timeout_duration": "60s"
    }
  }
}
```

2. ophalen database id, want die is nodig voor koppelen aan Databricks app qua rechten

```bash
database_id=$(databricks api get --profile ${{ parameters.environmentName }} api/2.0/postgres/projects/${{ parameters.databricksAppsName }}/branches/production/databases | jq -r ".databases[] | select(.status.postgres_database == \"${{ parameters.databaseName }}\") | .status.database_id")
```

3. maak een volume aan indien nodig

```bash
databricks volumes create --profile ${{ parameters.environmentName }} catalog_${{ parameters.environmentName }} schema_${{ parameters.volumeName }} volume_${{ parameters.databricksAppsName }} MANAGED
```

4. maak app aan met koppelingen

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/apps --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/app.json"
```

met als json payload

```json
{
  "name": "${databricksAppsName}",
  "description": "${appDescription}",
  "budget_policy_id": "${budgetPolicyId}",
  "git_repository": {
        "url": "https://xxx@dev.azure.com/organisation-name/project-name/_git/repo-name",
        "provider": "azuredevopsservices"
      },
  "resources": [
    {
      "name": "database",
      "postgres": {
        "branch": "projects/${databricksAppsName}/branches/production",
        "database": "projects/${databricksAppsName}/branches/production/databases/${databaseId}",
        "permission": "CAN_CONNECT_AND_CREATE"
      }
    },
    {
      "name": "volume",
      "uc_securable": {
        "securable_full_name": "catalog_${environmentName}.schema_${databricksAppsName}.volume_${databricksAppsName}",
        "permission": "WRITE_VOLUME",
        "securable_type": "VOLUME"
      }
    },
    {
      "name": "job",
      "job": {
        "id": "${databricksJobId}",
        "permission": "CAN_MANAGE_RUN"
      }
    }
  ],
  "telemetry_export_destinations": [
    {
      "unity_catalog": {
        "logs_table": "catalog_${environmentName}.schema_${databricksAppsName}.${databricksAppsName}_logs",
        "metrics_table": "catalog_${environmentName}.schema_${databricksAppsName}.${databricksAppsName}_metrics",
        "traces_table": "catalog_${environmentName}.schema_${databricksAppsName}.${databricksAppsName}_traces"
      }
    }
  ]
}
```

5. update permissies op app

```bash
databricks api patch --profile ${{ parameters.environmentName }} /api/2.0/permissions/apps/${{ parameters.databricksAppsName }} --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/app_permissions.json"
```

met als json payload

```json
{
  "access_control_list": [
                          {
                            "group_name": "group-name",
                            "permission_level": "CAN_MANAGE"
                          },
                          {
                            "service_principal_name": "${{ parameters.serviceConnection }}",
                            "permission_level": "CAN_MANAGE"
                          }
                          {
                            "user_name": "user@name.nl",
                            "permission_level": "CAN_MANAGE"
                          }
                        ]
}
```

6. haal app service principal id op (voor rechten op database en GIT config)

```bash
app_details=$(databricks api get --profile ${{ parameters.environmentName }} /api/2.0/apps/${{ parameters.databricksAppsName }})
service_principal_id=$(echo "$app_details" | jq -r '.service_principal_id')
```

7. haal de git credential entry van de service principal op

```bash
databricks api get --profile ${{ parameters.environmentName }} /api/2.0/git-credentials?principal_id=${service_principal_id}
git_credential_id=$(databricks api get --profile ${{ parameters.environmentName }} /api/2.0/git-credentials?principal_id=${service_principal_id} | jq -r '.credentials[] | select(.git_provider == "azureDevOpsServices") | .credential_id')
```

8. maak git credential aan (indien je een PAT gebruikt zorg dan voor readonly access)

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/git-credentials --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/managed_identity_git.json"
```

met als payload

```json
{
    "name": "git-credential-name",
    "principal_id": "${servicePrincipalClientId}",
    "git_provider": "azureDevOpsServices",
    "git_email": "user@name.nl",
    "git_username": "user@name.nl",
    "personal_access_token": "xxx"
}
```

9. voer een deployment uit op de app zodat de source goed start als hij gestart wordt

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/apps/${{ parameters.databricksAppsName }}/deployments --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/deployment.json"
```

met als payload

```json
{
    "git_reference": {
        "branch": "main",
        "source_code_path": "databricks/resources/apps/${{ parameters.databricksAppsName }}"
      },
    "git_source": {
        "branch": "main",
        "source_code_path": "databricks/resources/apps/${{ parameters.databricksAppsName }}"
      }
}
```

10. start de app

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/apps/${{ parameters.databricksAppsName }}/start
```

11. maak een role aan op database voor de app service principal (en haal daarvoor service principal client id op)

```bash
app_details=$(databricks api get --profile ${{ parameters.environmentName }} /api/2.0/apps/${{ parameters.databricksAppsName }})
service_principal_client_id=$(echo "$app_details" | jq -r '.service_principal_client_id')
```

```bash
databricks api post --profile ${{ parameters.environmentName }} /api/2.0/postgres/projects/${{ parameters.databricksAppsName }}/branches/production/roles --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/database_role_sp.json"
```

met als json payload

```json
{
    "spec": {
        "attributes": {
            "bypassrls": true,
            "createdb": false,
            "createrole": false
        },
        "membership_roles": [
            "DATABRICKS_SUPERUSER"
        ],
        "auth_method": "LAKEBASE_OAUTH_V1",
        "identity_type": "SERVICE_PRINCIPAL",
        "postgres_role": "${servicePrincipalClientId}"
    }
}
```

12. bescherm de productie branch op de database

```bash
databricks api patch --profile ${{ parameters.environmentName }} /api/2.0/postgres/projects/${{ parameters.databricksAppsName }}/branches/production?update_mask=spec --json @"$(Build.SourcesDirectory)/pipelines/json/${jsonFilePrefix}/database_branch.json" 
```

met als json payload

```json
{
  "spec": {
    "is_protected": true,
    "no_expiry": true
  }
}
```

13. haal de ruleset voor de service principal van de app op zodat je de etag krijgt

```bash
rule_set_response=$(databricks api get --profile ${{ parameters.environmentName }} "/api/2.0/preview/accounts/access-control/rule-sets?name=accounts/${{ parameters.databricksAccountID }}/servicePrincipals/${service_principal_client_id}/ruleSets/default&etag=" || echo "")
```

en de etag

```bash
etag=$(echo "$rule_set_response" | jq -r '.etag // ""')
```

14. voeg je aanpassingen door op de ruleset en update ze dan

```bash
databricks api put --profile ${{ parameters.environmentName }} \
                    /api/2.0/preview/accounts/access-control/rule-sets \
                    --json "{
                      \"name\": \"${rule_set_name}\",
                      \"rule_set\": {
                        \"name\": \"${rule_set_name}\",
                        \"grant_rules\": ${merged_grants},
                        \"etag\": \"${etag}\"
                      }
                    }"
```

Uiteraard kan je deze stappen allemaal mooi dynamisch maken door eerst wat GETs ervoor te zetten en te updaten/patchen indien nodig. 
(Dat heb ik ook maar dan zou de blogpost nog veel langer worden..) 
Dan werkt het allemaal best mooi. 
Blijft wel de vraag of al deze stappen zo in 1 bundle terecht kunnen komen of dat je altijd met een hybride aanpak blijft hangen waarbij je bundles en CLI en/of API nodig hebt. 
Voorlopig werkt dit ieder geval prima. 
En her en der mis je wat stukken code maar dat vooral op de dynamische aanpassingen die nodig zijn voor rechtenbeheer en groepen wat je simpel in bash/powershell/python kunt doen. 
Op deze manier heb je ieder geval wel alle benodigde syntax voor de Databricks APIs die werkt op 1 plek.
