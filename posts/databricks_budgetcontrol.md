---
title: databricks budgetcontrol
date: 2026-08-17
description: de ontwikkeling van databricks als platform vraagt om betere rbac en budget control mogelijkheden
---

# databricks budgetcontrol

Nog niet lang geleden was Databricks een simpel data science product wat je altijd neerzette in een landschap om data scientists te voorzien in een tool die veelzijdiger was en meer maatwerk mogelijk maakte dan de AWS/Azure native tooling. 
De tijd dat Databricks een simpele tool is om wat Spark loads en vooral machine learning loads te faciliteren lijkt alweer even voorbij te zijn. 

Databricks wordt steeds meer een "platform" waarbij eigenlijk alle mogelijke data opties die je zou willen realiseren erin afgehandeld kunnen worden. 
Beetje bij beetje absorbeert het diverse tooling die je eerder wel nodig had in je opzet. 

Orchestratie > Jobs en workflows
Dashboards > AI/BI Dashboards
Data applicaties/dashboards zoals Streamlit > Databricks apps
Kleine CRUD apps > Databricks apps + Lakebase(PostgreSQL)
AI agents > Agent Bricks / Genie
(gen)AI Model serving > Model serving / Foundation Models
API gateway > AI Gateway
Catalog > Unity Catalog
Data quality > Lakehouse monitoring
Metadata > Unity Catalog
Data warehousing > SQL Warehouse
ETL > Lakeflow / pipelines
Alerts > SQL Alerts
Access management > Unity Catalog permissions & policies

Voorheen waren dit eigenlijk allemaal losse onderdelen die je aanvullend aan Databricks inregelde en een keuze maakte qua architectuuropzet hoe je dit wilde doen en welke tool je erbij wilde halen. 
Doordat Dataricks alles P*Q op gebruik aanbiedt zonder ingewikkelde licentiestructuur zie je dat er een sterke aanzuigingskracht is om voor de Databricks native tool te gaan. 
Dit leidt wel tot grotere lock-in en een hoop van de aanvullende tooling en services zijn niet opensource en zijn dus bij een stap naar een ander platform een extra barriere die je moet nemen.  

Aanvullend met al deze nieuwe producten is de noodzaak om in control te zijn over je inrichting en de kosten die al die services potentieel kunnen maken erg belangrijk. 
Initieel richtte je bewust spark clusters in die je wilde gebruiken en was je met een auto shutdown tijd al relatief ver. 
Nu is de situatie echter zo dat praktisch elk onderdeel binnen het lijstje hierboven om extra configuratie vraagt om te zorgen dat je bij grootschalige inzet niet opeens met ongewenste kosten wordt opgescheept. 

Dit wordt nog eens versterkt door het feit dat je Databricks als evolving product afneemt waarbij het zichzelf continue update, wat een voordeel is maar in enterprise settings ook zeker af en toe een nadeel. 
Bij ieder subproduct wat wordt toegevoegd zal dit eerst voor het totale publiek openstaan en niet direct cost en budget control ingericht zijn. 
Dit leidt af en toe simpelweg tot een bodemloze put wat in een enterprise setting eigenlijk resulteert tot een product wat je niet kan en moet willen inzetten. 

Databricks als platform kan resulteren in enkele gebruikers die >1k kosten per maand kunnen maken door producten als Genie en serverless compute indien je de standaardinstellingen hanteert. 
Correcte RBAC inrichting om dit onder control te brengen is voor sommige onderdelen simpelweg niet mogelijk en verreist intern detectie en politiewerk wat zeer ongewenst is. 

Alternatief hiervoor is Databricks puur inzetten als creatie tool waarbij je een gericht gezelschap toegang geeft tot het platform. 
Dit gaat dan wel weer in tegen de gedachte dat Databricks de tool voor meerdere data rollen zou moeten zijn. 
Budgettaire angst zou geen reden moet zijn om een tool te kunnen inzetten en betekend eigenlijk dat er simpelweg iets mist. 
Wellicht is dit het resultaat van een tool dat dermate dominant op de cloudmarkt is dat er geen echte concurrenten bestaan die ervoor zorgen dat de checks en balances van een platform ook goed ingericht zijn omdat anders concurrentie het grote publiek er wel op zouden wijzen en een verbeterslag zouden afdwingen. 
Of het resultaat van een steeds groter bedrijf dat haar ontwikkelsnelheid wil behouden. 
Accepteren dat je snel nieuwe producten kunt releasen zonder dat gewenste enterprise features ingebakken zijn in de nieuwe mogelijkheden. 
Dit terwijl dit initieel mogelijk wel de reden was dat partijen voor de tool/platform kozen. 

Voor nu zijn de opties simpelweg; de mensen hebben om de tool juist te configureren en dan alsnog harde alerts en correcties afdwingen voor onderdelen zoals model serving, serverless en apps die nog niet goed te budgetteren en/of te RBAC'en zijn. 
Of mensen onboarden met SQL only access en daarmee een groot deel van het platform niet inzetten waarmee de vraag opdaagt waarom je niet een andere tool of platform zou inzetten waarbij cost control en RBAC wel beter is ingericht en voldoet aan de eisen om het in te zetten op en platform met duizenden gebruikers waarbij handmatig cost control nooit gaat werken. 

Hopelijk komt Databricks met simpele effectieve RBAC/budget control in de toekomst voor alle onderdelen zodat een keuze voor Databricks niet perse een blinde gok is met een grote opwaartse kostentrend. 
De vraag is ook nog hoe erg dit zal zijn in de toekomst voor een bedrijf dat de kwartaallijkse drang voelt om goede financiele cijfers te presenteren. 
Qua funding rounds loopt Databricks toch alweer bijna uit het alfabet. 
