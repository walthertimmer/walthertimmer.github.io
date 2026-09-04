---
title: hoe lang zijn ai agents nog veilig
date: 2026-09-04
description: wanneer zullen llm grootschalig worden ingezet voor cyberattacks of surveillance? 
---

# hoe lang zijn ai agents nog veilig?

Er wordt steeds meer een stap gemaakt van simpelweg chatbots met LLMs naar een werkmodus met GenAI waarbij agentic workflows de norm worden. 
Bij de simpele chat applicaties zit er simpelweg aan de kant nog een "human in the loop" om te kijken of het resultaat ergens op slaat en om het in te zetten in wat voor manier dan ook.

Met de agentic flows, wat effectief veelal simpelweg markdown "skills" zijn, is er een mogelijkheid voor een AI "harness" (een ingewikkelde for loop) om verschillende commando's lokaal te draaien waar de AI chatbot of agent draait. 
Het ligt natuurlijk aan je configuratie maar je ziet bij de meeste harnesses dat bash en welke programmeertaal dan ook een mogelijkheid is. 
Effectief staat de omgeving of sandbox waar je agent staat volledig open voor wat er vanuit de LLM kan verschijnen. 
Al dan niet afgevangen met AI guardrails die de ergste vergrijpen zouden moeten tegengaan qua software attacks die uit de LLM zouden kunnen verschijnen. 

Nu is eigenlijk elke AI een black box qua trainingsdata dus erg moeilijk te doorgronden wat er in potentie allemaal uit een LLM zou kunnen verschijnen. Ook een open weight model bevat eigenlijk nooit de oorspronkelijke trainingsdata of de totstandkoming van het model. 
In potentie zou je dus LLMs kunnen trainen om een rol te vervullen in de cyber attacks van de toekomst zonder dat gebruikers dit weten. Helemaal als je gratis open weights modellen aanbiedt die veelvuldig gebruikt worden. 
Dit vergt wel een lange termijn blik en een kleine gok over wie je modellen gaan gebruiken. Amerikaanse modellen zullen vaak door Amerikanen gebruikt worden en Chinese modellen door Chinese bedrijven. 
Alleen de laatste tijd zie je alleen maar grote open weight frontier modellen vanuit Chinese landen. 
Dit betekend dus dat als je open weight modellen wilt gebruiken als bedrijf of overheid en je ook nog een cutting edge technologie wilt je Chinese modellen dient te gebruiken. 
Een interessante positie voor China. 

Buiten het model zelf zie je ook overal een tekort aan GPUs om een invulling te geven aan de GenAI LLM behoefte intern wat ervoor zorgt dat veel bedrijven en overheidspartijen gebruiken maken van remote of cloud AI modellen. 
Wetende dat deze nu steeds vaker gekoppeld worden aan agents die blind uitvoeren wat voor commando ze van hun remote model krijgen maakt een lokale agent met een remote LLM je kwetsbaar. 
Helemaal nu er een sterke marketing push is om agents te koppelen aan MCP/APIs van bestaande systemen. 
Als de agent gehackt wordt is je fallout dus groter dan die ene sandbox. 

Daarnaast maakt de grote inzetbaarheid van LLMs voor informatie intensieve taken ze eigenlijk extreem interessant om af te luisteren. 
Waar het voorheen vooral om internetkabels en spectrums die afgeluisterd werden ging; zal het in toekomst waarschijnlijk gaan om grote afluistersystemen rondom de LLM modellen. 
Een router die voor alle cloudpartijen de diverse documenten en tokens die richting de modellen gaat op basis van eindgebruiker nog naar een extra partij routeert. 

Al deze risico's zorgen er eigenlijk voor dat hoe economisch efficiënt cloud modellen kunnen zijn airgapped modellen eigenlijk de enigste keuze zijn voor agents die je in operationele workloads wil inzetten als je iets interessants wilt doen. 
Het is misschien nog even wachten op de eerste grote voorbeelden...
