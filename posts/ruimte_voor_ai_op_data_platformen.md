---
title: ruimte voor ai op data platformen
date: 2026-09-24
description: welke componenten dienen er voor ai ingevuld te worden op een data platform
---

# ruimte voor ai op data platformen

Ooit zat er vooral een heel sterke datawarehouse focus op data platformen; of eigenlijk databases. 
Eén grote database kon voorzien in de informatiebehoefte van een organisatie door een bron te zijn voor alle dashboarding. 
Op termijn kwam daar voor steeds meer organisaties een machine learning behoefte bij en ook data hoeveelheden die niet altijd logisch en performend in 1 database waren te proppen.  
Nu is een Datalake of swamp groot goed voor veel enterprises en niet alleen maar iets van big tech. 

Daar komt tegenwoordig met AI, wat effectief de grote verzamelnaam is voor het veld waar het eerder genoemde machine learning ook gewoon onder valt, weer een extra behoefte bij. 
Voor de invulling van AI, of eigenlijk GenAI, zijn er extra functionaliteiten die ingevuld moeten worden op een ‘modern’ dataplatform. 

In de meest simpele vorm dient er een P*Q mogelijkheid te zijn voor het afnemen van GenAI workloads van 1 of meerdere cloud providers. 
Of een simpele fysieke server met GPUs die puur en alleen dient om een vLLM endpoint aan te bieden aan andere processen in de organisatie. 
Dit kan allemaal ingericht worden op open weight modellen die vanuit Huggingface worden ingeladen. 

Samenhangend met het verzorgen van het aanbieden van GenAI modellen zal er ook een behoefte zijn voor agent sandboxes, of microVMs, om de loops tegen de endpoint uit te voeren. 
Dit kan er simpelweg eentje zijn om te voorzien in de eigen custom chatapplicatie a la ChatGPT. Frameworks als Open WebUI of LibreChat kunnen hierin voorzien. 

Met de agents komt ook de vraag welke vibecoded framework (of meerdere) je introduceert om te voorzien in agentic werk. 
Veel van de frameworks zijn zo groot en hebben zulke hoge ontwikkelsnelheden dat je ze eigenlijk onmogelijk kunt controleren voor veilig enterprise gebruik. 
Of je doel moet natuurlijk zijn om een "uitbrekende" agent te hebben voor PR doeleinden. Interessant fenomeen dat bestaande cyberwetgeving niet meer lijkt te bestaan als je een agent laat hacken. 

Door de groei van modellen en de diverse gebruikers krijg je vanzelf de behoefte om budgetten en limieten in te stellen voor je GenAI gebruik en dus ook de noodzaak om een AI gateway in te richten die je hierbij kan helpen. 

De vervolgstap voor operationeel gebruik is de mogelijkheid om de modellen te finetunen met eigen data en gefocused op inzet in eigen processen. 
Idealiter is dit een werkplek die zowel hierin kan voorzien als ook de klassieke machine learning zodat je niet volledig losstaande componenten blijft toevoegen en beheerslast nog enigszins controleerbaar blijft. 

En dan komt het leukste onderdeel; hoeveel toegang durf je de nieuwe AI loads te geven tot je bestaande systemen en hoe organiseer je dat veilig en auditproof. 

Zodra de productie workloads eenmaal draaien komt ook de behoefte om ze actiever te kunnen monitoren en te kunnen testen met diverse finetuning en nieuwe modellen van andere providers. 
Idealiter kun je continue A/B tests uitvoeren en zo bijsturen. 

Daarnaast is er natuurlijk ook de harde bijstuurbehoefte door middel van AI guardrails. 
Zodra een model hallucineert moet het afgepakt worden en ook veel modellen zijn relatief eenvoudig hackbaar voor ongewenst gedrag indien ze in contact komen met niet altijd goed gescreende data. 

Genoeg nieuwe componenten die ingevuld dienen te worden waarbij op dit moment nog geen eenduidige winnaars in de markt zijn aan te wijzen. 

