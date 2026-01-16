---
title: CloudNativePG backups naar object storage
date: 2025-09-17
description: Hoe kan je CloudNativePG backuppen naar storage accounts? 
---

# CloudNativePG backups

PostgreSQL is min of meer de defacto standaard voor het ondersteunen van OLTP workloads als je opensource tooling wilt gebruiken. Nu kan je PostgreSQL direct installeren op een VM of server maar je kan het tegenwoordig ook prima op Kubernetes draaien en daarmee een gedeelte van het instellen van read-replicas en failover van primaire databases automatiseren. 

Hierbij is het belangrijk dat je ook backups buiten het kubernetes cluster hebt mocht het cluster falen of de onderliggende storage volumes problemen vertonen. Een methode voor dit alles is CloudNativePG gebruiken en de bijbehorende backup en Write-Ahead Logging (WAL) files weg te schrijven naar een extern S3 storage account. 

Online zijn hier niet gemakkelijk volledig ingevulde voorbeelden te vinden vandaar bij deze.

De CNPG backup config voor WAL files naar Cloudflare:

```bash
# Backup configuration (optional)
  backup:
    retentionPolicy: 30d
    barmanObjectStore:
      endpointURL: https://xxx.r2.cloudflarestorage.com/postgres
      destinationPath: "s3://postgres/"
      s3Credentials:
        accessKeyId:
          name: cnpg-s3-creds
          key: S3_ACCESS_KEY
        secretAccessKey:
          name: cnpg-s3-creds
          key: S3_ACCESS_SECRET
      wal:
        compression: gzip
        maxParallel: 8
```

en de backup zelf richting cloudflare:

```bash
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata:
  name: backup-shared-postgres
  namespace: cnpg
spec:
  schedule: "0 0 0 * * *" # every day at midnight
  backupOwnerReference: self
  target: "prefer-standby" 
  method: "barmanObjectStore"
  immediate: true
  suspend: false
  cluster:
    name: shared-postgres
```

of richting Hetzner object storage:

```bash
# Backup configuration (optional)
  backup:
    retentionPolicy: 30d
    barmanObjectStore:
      endpointURL: https://nbg1.your-objectstorage.com
      destinationPath: "s3://<bucket-name>/postgres/shared-postgres/"
      s3Credentials:
        accessKeyId:
          name: cnpg-s3-creds
          key: ACCESS_KEY
        secretAccessKey:
          name: cnpg-s3-creds
          key: ACCESS_SECRET
      wal:
        compression: gzip
        maxParallel: 8
```

en zo kan je dit ook doen voor bijvoorbeeld Scaleway als S3 provider:

```bash
# Backup configuration (optional)
  backup:
    retentionPolicy: 30d
    barmanObjectStore:
      endpointURL: https://s3.nl-ams.scw.cloud
      destinationPath: s3://<bucket-name>/cloudnativepg/
      s3Credentials:
        accessKeyId:
          name: cnpg-secret
          key: AWS_ACCESS_KEY_ID
        secretAccessKey:
          name: cnpg-secret
          key: AWS_SECRET_ACCESS_KEY
        region:
          name: cnpg-secret
          key: AWS_S3_REGION_NAME
      wal:
        compression: gzip
        maxParallel: 8
```

In die overige gevallen blijft de backup zelf identiek want die gebruikt de settings van het cluster. 
Met deze backups is het ook mogelijk om een nieuw cluster te starten dat zelf de data inlaadt. 
Handig voor een herstart op een nieuw cluster of het draaien van wat performance tests of een database met dezelfde hoeveelheid data als je productie omgeving. 

Zie verder vooral ook: [cnpg barman documentatie](https://cloudnative-pg.io/documentation/1.25/backup_barmanobjectstore/)
