---
title: Open source data platform
date: 2025-11-26
description: Gedachtes over een open source data platform. Hoe kan dit eruit zien? Welke tooling komt erbij kijken? En waar moet je aan denken?
---

# Open source data platform

Als bedrijf en/of overheidsorgaan wil je voor sommige data gebruik maken van een eigen on premise platform i.v.m. data gevoeligheid, wettelijke eisen of het vermijden van een vendor lock-in. Vroeger was dit allemaal een stuk lastiger met opensource tooling die ontbrak of simpelweg erg ondermaats was in vergelijking tot de tooling die commercieel aangeboden werd. Veel van de tooling is robuuster geworden en met vergaand devops / infrastructure as code is het beheer ook laagdrempeliger geworden zolang je niet de limieten opzoekt van wat mogelijk is. Voor veel big tech is dat zeker het geval, voor veel Nederlandse partijen is dit zeer zeker niet het geval. 

Het hedendaagse eisenpakket van een data platform is wel wat veranderd nu iedereen ook een plek wilt voor het ontwikkelen en hosten van RAG / GenAI apps die vaak toegevoegde waarde hebben mits ze bij interne data en documenten kunnen. Zowel Snowflake als Databricks als commerciële partijen springen hier op in met de mogelijkheid om apps in het platform te draaien. Een soort cloud in de cloud ervaring. Daarnaast blijven batch jobs en soms streaming jobs de hoofdzaak van een data platform met een dashboarding tool die erop aansluit. Dit aangevuld met een solide storage service en een query service erbovenop zodat de dashboard tool ergens tegen kan praten. Veel dashboard tools kunnen technisch wel direct tegen storage praten maar in praktijk werkt of schaalt dit niet. 

Daarnaast heb je natuurlijk ook wat randzaken die je verder in wilt richten voor een beetje data platform en wil je dit alles ook nog beheersbaar houden. Wat vooral betekend dat je qua FTE die je nodig hebt voor puur onderhoud van het platform niet te hoog wilt zitten. Europa is relatief tot de VS een lage lonen land maar het telt wel door. Een hoog aantal minimum FTE om een platform draaiend te houden betekent ook dat het voor veel partijen niet te doen is om niet voor een commerciële partij te kiezen. (Buiten het feit dat je tegenwoordig geluk moet hebben om de juiste mensen uit de markt te halen.) 

En je hebt natuurlijk de keus; zijn alle zaken relevant qua eisen en wensen. Is er daadwerkelijk een business case voor streaming die ook daadwerkelijk positief uitkomt als je rekening houdt met de kosten van een complexere setup en meer beheerslasten. 

Eigenlijk zou je qua tooling ook niet volledig vast willen zitten op x of y maar meer een transparante setup hebben waarbij je bepaalde peakload in de cloud of extern kan uitbesteden en je dus de keuze hebt waar je een job draait. Een echt open data platform waar je tools kunt inwisselen voor best of class, want dat wisselt nogal eens. Of je eigen eisen en wensen verschuiven. 

Een plaatje geeft soms ook wat meer duiding. Zie onder. Realiteit is echter dat bij elke tooling en keuze er nog een aantal andere software pakketten zijn die in hetzelfde kunnen voorzien dus dat maakt het des te belangrijker dat de tooling flexibel is in data opzet en het uitwisselen van data. Je kan effectief met een data platform beginnen en dan periodiek hereiken kijken waar de pijnpunten zitten en de specifieke tool waar de meeste uitdagingen zitten vervangen met iets anders. 

![Open source data platform](../images/opensource_dataplatform.svg)

Ook staan er enkele assumpties aan ten grondslag. Hoe open moet de software zijn? Welke licentie is goed genoeg? Wat is de schaal van je totale data? Bij grotere hoeveelheden wil je Minio waarschijnlijk vervangen. Bij kleinere hoeveelheden data kan je met Polars aan de gang in plaats van Spark met al haar overhead. Of is de data hoeveelheid dusdanig dat je het er allemaal tussenuit haalt en samenvoegt tot 1 Postgres instantie met de juiste extensie om tabellen wel voor OLAP geschikt te maken? Of ga je juist de andere kant op qua hoeveelheden en eisen qua performance van je dashboarding en kom je eerder op een Clickhouse uit? Hoe ziet je data eruit? Is de grootste gedeelte van je data wel gestructureerd of zit je meer in de geo hoek? 

Bij het zelf samenstellen van je open source data platform zijn er veel meer keuzes te maken qua tooling en ook veel meer te POC'en omdat niet altijd alle tooling goed samenwerkt. Dat is toch wat anders dan wat de grote cloud providers plus Databricks, Snowflake en Clickhouse aanbieden. Zij bieden de mogelijkheid om het totale plaatje, waarbij ik nu bewust nog wat zaken weglaat, te vervangen met slechts 1 icoon. Misschien niet best in class op elk gebied maar wel gemakkelijk een hele grote sprong maken naar een data platform dat praktisch alle facetten afdekt. 
