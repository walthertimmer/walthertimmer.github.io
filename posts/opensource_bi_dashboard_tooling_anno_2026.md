---
title: opensource bi dashboard tooling anno 2026
date: 2026-05-22
description: wat zijn op het moment concreet opties qua opensource BI dashboard tooling die voldoen aan globale enterprise eisen
---

# opensource bi dashboard tooling anno 2026

Er is een hele rits aan hippe open dashboards die gebruikt kunnen worden voor business intelligence (BI). Wat je echter ziet is dat de meeste gestart worden met venture capital en daarmee een bepaald marktaandeel hopen te pakken om daarna features uit de opensource variant te halen of beheersbaarheid moeilijker te maken om maar te up sellen naar het betaalde product. Of het product was dusdanig succesvol dat 1 van de reeds bestaande data bedrijven het opkoopt en dan is het altijd de vraag of het open blijft en of de ontwikkeling door blijft gaan. Dit wisselt nog weleens per opkopende partij. 

Voor kleinere organisaties met lagere eisen zijn er nog wel meer mogelijkheden maar als je wat groter bent als organisatie en bepaalde eisen dient te stellen op logging, audit, RBAC en SSO vallen er een hele hoop tools af. 

Ook zijn er nieuwere hippere tools die zich richten op "BI as code" wat wil zeggen dat deze rapportages en dashboards eenvoudig zijn op te slaan en te reviewen in GIT. Handig als je werkt met een tech savvy populatie in je organisatie. 

Er zijn ook een hoop open python/javascript libraries voor visualisatie maar die laat ik buiten beschouwing omdat die niet eenvoudig zijn in te zetten om een grote set analisten in corporate verband dashboards te laten bouwen. In de meeste corporate omgevingen zullen mensen simpelweg niet vrijelijk Python en code tools kunnen installeren op hun laptops om visualisaties te bouwen. 

## metabase

1 Van de grotere open BI tools. > 1.3k PRs en >70 auteurs op de PRs op Github afgelopen maand.  Ook een erg gebruiksvriendelijke tool die analisten via website kan bedienen. Belangrijke zaken zoals SSO, inzicht in gebruik, audit, RLS en RBAC zitten allemaal in de enterprise variant en worden bewust uit de OSS variant gehouden. Zie [documentatie](https://www.metabase.com/pricing/).

## evidence.dev

Zo'n coole "BI as code" tool uit Canada. Lijkt er wel op dat de private equity squeeze iets te snel kwam en daardoor het project volledig dood is gebloed en alles nu in Evidence studio zit wat niet zo open en vrij is. 0 PRs afgelopen maand. 

## redash

Ooit groot en hip met de mogelijkheid om alles in de web browser te ontwikkelen. Gekocht door Databricks en daar Databricks Dashboards AI/BI geworden. Is een aantal jaar volledig stil geweest op de repo maar in ~2025 een nieuwe groep vrijwilligers die het project weer op willen pakken en verder willen ontwikkelen. Puur op activiteit op Github is dat echter nog steeds een erg minimale groep mensen en de meeste partijen zijn er vanaf aan het migreren. 

## lightdash

De BI tool die het meest geïntegreerd is met DBT. Als je dat dus niet gebruikt heeft het weinig waarde. Daarmee ook erg afhankelijk van DBT. > 800 PRs en 30 auteurs. Iemand heeft agentic AI gevonden.. Is onlangs geshift qua aanpak op een volledig "agentic" flow waarbij agents de dashboars bouwen. Green groepbeheer in de OSS en SSO. Verder is de API in de OSS ook niet open dus geen gemakkelijke CI/CD pipeline opties. 

## grafana

Effectief de timeseries dashboarding tool die heel erg breed wordt ingezet. Grafana labs richt zich daarbij vooral op support en enterprise contracten maar lijkt verder geen gerichte beperkingen op de OSS variant te plaatsen. >1500 PRs en >200 auteurs. Effectief dus de breedst gedragen tool van allemaal. RBAC wordt helaas wel alleen in de enterprise variant gefaciliteerd en daarom niet de handigste tool om in te zetten voor BI als je volledig OSS wil gaan. 

## superset

Netjes beheerd door de Apache foundation. >600 PRs en 90 auteurs afgelopen maand. Een van de grootste en bekendste dashboarding tools die verschillende modussen biedt voor diverse soorten gebruikers. Zowel no-code als SQL. Een gigantische set aan ondersteunde onderliggende [databases](https://superset.apache.org/user-docs/databases/).  Biedt RBAC, biedt embedding, heeft een onderliggend API model voor het inrichten van CI/CD. Verder een gigantische set aan visualisatie types die ondersteund worden, zowel relationeel als geo mogelijkheden. En plugin opties. 

## shaper (taleshape) 

Een hippe nieuwe dashboarding tool die inzet op o.a. DuckDB om snelle dashboards te realiseren. Zet vol in op de BI as code workflow waarbij je je dashboards als SQL kunt bouwen en op kunt slaan in SQL. Is op het moment druk bezig met het bouwen van de managed (cloud) oplossing van de tool. Op dit moment pushed het er nog op dat alle features ook in de OSS variant zitten; zaken zoals embedding. Afgelopen maand >40 PRs met 2 auteurs waarvan [1 bot](https://github.com/taleshape-com/shaper/pulse?period=monthly). Niet echt een robuuste community om als enterprise op in te springen.

## pentaho reporting

Voornamelijk een report tool dan een dynamische BI tool. Met 11 PRs en 4 auteurs ook niet echt booming.

## Eclipse BIRT (Business Intelligence and Reporting Tools)

Afgelopen maand 3 PRs van 2 auteurs. Het bestaat nog, en ook al lang, maar lijkt niet meer echt een bewuste keuze als je nu aan de gang wilt. Ook qua UI en werkwijze niet echt meer meegekomen met de huidige opties qua commerciële tooling. 

## KNIME 

Een opensource visualisatie platform waarbij code publiek is maar geen eenduidige manier om voor een self hosted variant te gaan. 

## Jaspersoft CE

Vooral een tool voor vaste rapportages en niet perse een BI tool die dynamische analyses mogelijk maakt. Erg niche. Erg dood. 

## Helical insight

Een soort dashboarding tool waarbij alle fijne UI driven mogelijkheden gegatekeeped zijn het enterprise product. Effectief dus niet echt een opensource tool, meer een trial.

## DataEase

Een grote Chinese OSS dashboarding tool. Helaas is bijna alles qua documentatie in het Chinees dus niet echt bruikbaar in het westen. 

## conclusie

Bovenstaande zijn de tools die eruit springen op internet/reddit en/of [github](https://github.com/topics/business-intelligence).  

De conclusie daarbij is dat als je timeseries data hebt of operationele systemen in de gaten wilt houden je voor Grafana kunt gaan. Iedere andere vorm van reporting is eigenlijk de enige keuze die je hebt Superset. Op zich wel een voordeel dat de gehele OSS community zich naar 1 tool dient te conformeren. 
  
