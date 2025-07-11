---
title: public cloud private cloud walther’s cloud
date: 2025-07-11
description: Wat draait er in mijn meterkast? Servers, clusters en cloud. 
---

# public cloud private cloud walther’s cloud

Werken met data betekend tegenwoordig veelal werken in de cloud. 
En de cloud is dan veelal 1 van de grotere Amerikaanse partijen die min of meer dezelfde services bieden. 
Denk aan managed oplossingen voor object storage, databases, dataverwerking en data visualisatie. 
En tegenwoordig natuurlijk reeks aan hippe tools met AI in de titel of als eindproduct. 

Je ziet dat tegenwoordig de producten steeds verder omhoog komen in de levering van de service. 
Waar we vroeger nog gedeelelijk VMs afnamen, zijn dit nu containers geworden of zelfs tooling die volledig serverless zijn gaan opereren. 
Eerder kon je veel nog los configureren maar vooral met serverless vervalt dat werk en is alles "as is" aangeboden. 
Vaak iets minder technische features maar toch ook minder beheer want er kan minder kapot gaat (in theorie). 
En als het kapot gaat kan je er zelf niks aan doen. 

Ondanks die nieuwe wereld is het handig, en leuk, om te zorgen dat je nog steeds de skillset hebt om bovenstaande tooling in te richten in een niet managed variant. 
Al is het maar om de absolute vendor lock-in qua kennisopbouw niet onbewust te activeren. 
Als je alleen nog simpele managed tooling gewend bent en niet meer weet hoe je een simpele VM of container hardened inricht op een beheersvriendelijke manier zit je altijd volledig vast aan de managed oplossingen. 
Ook als die managed oplossingen soms simpelweg niet zijn toegestaan door compliance of qua kosten/performance totaal niet uitkomen met de zelf beheer variant. 

Hiervoor heb ik thuis een apart virtual network ingericht voor servers die toegankelijk moeten zijn voor het internet met een web application firewall (WAF) ervoor. 
En uiteraard blocking rules zodat dit network niet kan praten met 1 van de andere netwerken die ik thuis heb ingericht. 

Op deze servers heb ik een Kubernetes cluster ingericht die verschillende tooling voor mij draait. 
Denk aan ArgoCD (orchestration van containers), Github Actions runner container (het builden en deployen met on-prem hardware), CloudnativePostgres, Ceph, diverse eigen applicaties als containers en Grafana en Kubernetes dashboard voor monitoring en alerting.  
Deze opzet biedt mij maximale vrijheid om nieuwe tooling uit te testen en ook een brede set aan kennis bij te houden. Van infrastructuur keuzes, network inrichting en uitrol van applicaties. 
Bovendien zie je eigenlijk met de uptime van symmetrische 1Gbit+ (tip: Odido biedt zelfs 8Gbit aan) glasvezellijnen dat de bittere noodzaak om altijd maar direct een VPS of container bij een hosting provider te huren niet altijd meer nodig is. 
Vooral als je ziet dat je voor een beetje managed postgres database toch gauw aan de 50+ euro per maand zit bij een cloud provider en ook VPSen met meer dan enkele GBs aan ram zijn vaak behoorlijk aan de prijs. 
Uiteraard zit een groot deel van de prijs ook in het verzorgen van de SLA maar voor kleinschalige zaken speelt dat wat minder. 
Al mijn applicaties zijn op Nederland gericht dus een beetje downtime in de nacht maakt eigenlijk niks uit. 

Het veilig inrichten en houden van een server is over de jaren heen eigenlijk ook veel simpeler geworden. 
Met de juiste image en wat standaard pakketten en een goed update beleid op je machines dek je veelal het meeste al af. 
Het is daarom eigenlijk jammer dat veel mensen eigenlijk alleen nog ervaring opbouwen met managed oplossingen in cloud omgevingen. 
Want ook in die omgevingen zul je af en toe issues hebben en met support tickets moeten werken. Idealiter is dan niet alles hocus pocus voor je. 
En zonder deze kennis is de kans op een goed vergelijk tussen managed oplossingen en de doe-het-zelf opensource moeilijk te maken. 
Hoe kan je immers inschatten wat het werk is bij de laatste oplossing als je geen idee hebt wat het werk eigenlijk inhoudt? 
Onbekend maakt het veelal groter en enger dan het is. 

En veelal is de cloud oplossing ook zeker de goedkoopste en slimste oplossing, vooral als je je beheerwerk niet vergenoeg automatiseert en voor ~1-3 ton per FTE beheerders moet verzorgen. 
Daarmee kan je aardig vooruit in de cloud waar de kansen op foute configuratie ook weer wat kleiner is. 
Zoals altijd is het antwoord; het hangt er vanaf.. 
