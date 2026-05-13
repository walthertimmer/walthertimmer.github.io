---
title: dashboards extern delen in azure context
date: 2026-05-13
description: welke opties heb je om extern rapportages te delen indien je gebruik maakt van Azure tooling zoals PowerBI?
---

# dashboards extern delen in Azure context

In de Azure wereld zijn er op het moment een hoop opties voor PowerBI om rapportages extern te delen. Dus expliciet inzichten delen met mensen buiten het bedrijf. Niet al deze opties zullen altijd beschikbaar zijn aangezien je vaak ook rapportages hebt die niet extern beschikbaar dienen te zijn en vanwege dataveiligheid en het verminderen van kansen op datalekken vaak zult uitkomen op basis restricties binnen PowerBI zoals het onmogelijk maken om random gastaccounts aan te maken en mensen buiten de tenant toe te voegen. Verder wil je netwerktoegang en apparaat toegang vaak ook verder beperken zodat je data niet op ieder random apparaat beschikbaar is mocht er een keer een account gecompromitteerd zijn. Ook wil je rekening houden met het feit dat overal extern delen met gastenaccounts toestaan ook risico's met zich meebrengt dat medewerkers per ongeluk toegang uitdelen op een gehele PowerBI workspace niet alles gedeeld had mogen worden. 

Microsoft geeft zelf een aantal opties aan:
- delen met gastaccounts (zal vaak afvallen afhankelijk van hoe vrij de policies zijn omtrent gastaccounts, external sharing binnen PowerBI tenant moet aanstaan) 
- delen via Microsoft teams (kan met gastaccounts buiten de organisatie maar moet je die wederom wel toestaan)
- publish 2 web (waarbij je rapportages en data altijd bereikbaar zijn voor iedereen met de link dus zorg dat het echt open is)
- embedded delen 

[Zie opties extern delen.](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-share-dashboards)

## licenties of toch capacity
 
Buiten dat het toestaan van gastaccounts een centraal onderdeel spelen in het kiezen tussen deze opties is er nog een belangrijk onderdeel waar je rekening mee dient houden bij deze opties; je dient je PowerBI/Fabric capacity te upgraden tot een bepaald formaat ("Only P SKUs and F SKUs F64 or larger let users with a Microsoft Fabric free license and the Viewer role use Power BI apps and shared content.") of je dient per externe gastaccount een extra licentie aan te schaffen. Op dit moment schommelen deze tussen 15 en 25 euro per maand. De genoemde F64 capaciteit is er vanaf 8783 euro per maand. Dus ergens rond de 600 of 400 externe gebruikers (indien je je capaciteit vooruit betaald) zit het omslagpunt om voor dedicated capaciteit te gaan in plaats van losse licenties. 

## embedding

Er is echter nog een route om al die licenties te ontlopen en dat is de embedded route waarbij je maar liefst de keuze hebt uit 3 embedding capacities, namelijk PowerBI Embedded, PowerBI Premium en Microsoft Fabric. Om het allemaal overzichtelijk te houden. Gelukkig zijn alle 3 wel geschikt om te gebruiken voor embedding voor extern gebruik dus dat maakt verder niet heel veel uit. Er hangen wel andere restricties aan zoals  de grootte van je datasets en het aantal directquery connecties wat ondersteunt wordt; [zie daarvoor hier](https://learn.microsoft.com/en-us/fabric/enterprise/powerbi/service-premium-what-is#semantic-model-sku-limitation). Als je naar F2 Fabric capacity kijkt (wat de nieuwste variant is) heb je al voor 274 euro per maand een capaciteit staan. Als je niet tegen andere limieten aanloopt is het dus vanaf 20-30 externe interessant om naar de embedded variant te kijken in plaats van het licentie model.

## databricks ai/bi

Ook Databricks is een "native" Azure keuze met AI/BI dashboards die steeds meer kunnen en in totaliteit geen licentie model kennen. Echter heeft het embedded javascript framework wel toegang nodig tot APIs van je Databricks workspace die niet toegankelijk zijn als je Databricks workspace in een eigen private network staat. Iets wat voor corporate gebruik hopelijk het geval is. Effectief dus geen optie.  

## on premise uitzondering

Mocht je niet perse vast zitten aan de online PowerBI service kun je ook nog uitwijken naar de on premise [PowerBI Report Server](https://learn.microsoft.com/en-us/power-bi/report-server/developer-handbook-overview). Deze kan je lokaal in een VM neerzetten, of doe eens gek, in een VM op Azure. Ook hierbij kan je gebruik maken van embedding mogelijkheden van PowerBI rapportages. De on premise variant is op het moment samen gewikkeld met je Microsoft SQL Server licentie dus vooral interessant als je die al ergens hebt draaien. 

## embedding plaatje

![DashboardExternDelen](../images/DashboardExternDelen.png)

Ga je all in op het Microsoft verhaal dan kom je uit op een variant van bovenstaand plaatje waarbij je een eigen applicatie kunt schrijven en deployen op Azure App Service of Container Service (of AKS) met de embedded dashboards die je wilt delen. Aangezien het doel extern delen is zal je idealiter eerst een WAF inzetten voor je externe verkeer bij je app komt waarna gebruikers via embedding dashboards kunnen bekijken. Aangezien er geen licenties komen kijken zul je werken met service pricipals die rechten hebben op data en toegang hebben tot de APIs van PowerBI en/of onderliggende services. 

## data gateway

Verder valt natuurlijk op dat je ook nog een gateway nodig hebt voor de connectie tussen Databricks (of andere on-premise bronnen) en Fabric/PowerBI online indien je bron niet publiek toegankelijk is. Hier zijn uiteraard ook 2 varianten van; de on premise gateway en de virtual network data gateway. Uiteraard heeft de nieuwere managed virtual network data gateway [nieuwe limieten en restricties](https://learn.microsoft.com/en-us/data-integration/vnet/overview) en zijn bepaalde mogelijkheden gekoppeld aan de size van je embedding capaciteit. Hou dus rekening met welk formaat datasets je werkt of je zult alsnog onverwacht je embedding capaciteit moeten upgraden. 

 ## conclusie

Je embedding mogelijkheden uitwerken voor externen zijn misschien meer een excelfeestje dan daadwerkelijk een technische uitdaging. 
