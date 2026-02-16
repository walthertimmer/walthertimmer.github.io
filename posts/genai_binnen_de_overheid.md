---
title: GenAI binnen de overheid
date: 2026-02-16
description: Welke productlagen bestaan er in het GenAI product en op welke van deze richten overheidspartijen zich?
---

# GenAI binnen de overheid

Er zijn eigenlijk drie lagen binnen het (gen)AI landschap waar je je op kunt focussen en specialiseren. Je kunt ze alledrie gezamenlijk doen maar veelal is dit qua kennis en opzet/doel niet gewenst voor een overheidsonderdeel. Zo heb je een natuurlijke focus voor ieder rijksonderdeel naar wat ze klassiek ook al uitvoeren met huidig werk. De lagen zijn:

- infrastructuur / interference 
- model ontwikkeling / training
- wrappers 

## infrastructuur

Waar alle grote commerciële partijen nu en masse praktisch alle computercomponenten opkopen voor het gehele jaar of zelfs daarna (denk aan GPUs, RAM, SSDs en HDDs) om nieuwe datacenters uit de grond te pompen die grootschalig zijn in te zetten voor AI-loads is het op dit vlak wat rustiger bij de overheid. Voor veel AI workloads zijn de voordelen in euro’s nog niet heel hard wat het moeilijk maakt om ~8-GPU systemen te kopen die bij drie ton beginnen of ver daarover gaan voor de topmodellen. En zolang je niet vol erop inzet en aanschaft behaal je ook niet de inkoopvoordelen die wel gewenst zijn om competitief te kunnen zijn met commerciële uitbaters. Zonder de topsystemen ben je qua groottes van modellen ook veroordeeld tot kleinere LLM modellen die niet de beste mogelijkheden geven en daarmee ook de meeste business cases kunnen realiseren. Enfin dit onderdeel van infrastructuur en interference is waar de hardcore IT overheidsonderdelen als DICTU, SSC-IT en ODC-Noord zich op richten. [Zie ook deze prachtige infosheet voor een overzicht van partijen.](https://www.tweedekamer.nl/sites/default/files/field_uploads/Schema%20ICT-organisaties%20binnen%20de%20rijksoverheid%20volgens%20de%20tijdelijke%20commissie%20ICT_tcm181-239829.pdf) Aanvullend hierop heb je ook nog de [AI fabriek van 200 mio in Groningen](https://www.rijksoverheid.nl/actueel/nieuws/2025/06/27/nederland-zet-in-op-200-miljoen-euro-voor-aifabriek-in-groningen) die puur op basis van naam ook nog een rol gaat spelen. Het lijkt er echter wel op dat de laatste meer geënd is op het trainen van modellen dan simpelweg draaien van modellen voor “simpel” gebruik binnen de overheid. 

## model ontwikkeling

Daarmee komen we op het tweede onderdeel van model ontwikkeling waar [GPT-NL](https://huggingface.co/GPT-NL) het op mag nemen tegen veel grotere partijen die zich minder aan copyright hoeven te houden. Op het moment gebruiken ze 88 GPUs waar met de nieuwe fabriek in Groningen een verhoging van zou moeten komen. Effectief zijn ze in (semi-)overheidsland de enigste partij op deze laag. 

## wrappers

En dan heb je nog de laatste laag; de wrappers. Waar er in San Francisco honderden of (tien)duizenden bedrijven zich bezig houden op dit vlak met het effectief inzetten van bestaande (gefinetunede) modellen om een business probleem op te lossen en zo de weg naar unicorn status te behalen. Zo heb je in overheidsland ook 100+ van deze wrappers. Er zijn ongeveer 1600 overheidsonderdelen en je ziet dat het aantal echt grote overheidsonderdelen natuurlijk een stuk lager ligt maar van deze partijen is iedereen met een variant op LLM-chat bezig en daarnaast ook diverse RAG of Agentic opzetten waarmee een automatiseringsslag gemaakt zou moeten kunnen worden. Dit is ook logisch want van alle lagen waar je op kunt instappen is dit de goedkoopste om op in te stappen en trots te melden dat je iets met AI doet. Al deze verschillende partijen die met een eigen invalshoek een wrapper aan het ontwikkelen zijn maakt het ook het interessantste laag om naar te kijken. 

De brede tools die worden ontwikkeld en losgelaten op gebruikers zorgen ervoor dat wrappers op diverse manieren worden gebruikt die je soms niet had voorzien. Het is een beetje de vraag of je altijd precies een business case kunt uitschrijven hoe de tool en model een bepaalde situatie (gedeeltelijk) kunnen automatiseren of dat je juist door het breed inzetten van zo’n tool en te kijken naar hoe gebruikers het inzetten tot business cases kunt komen die je moeilijk zelf vooraf had kunnen verzinnen. Veelal weten de mensen op hun eigen vakgebied het beste hoe een tool ingezet kan worden en verlichting kan brengen. En op deze bevindingen kan je de generieke tools dan weer verder verfijnen. Of een dedicated tool ontwikkelen als het grootschalig interessant blijkt te zijn qua impact. 

Verder zijn een groot aantal van de wrappers tools die specifiek toe zijn geschreven op een specifieke handeling. Grote hamvraag blijft hierbij hoe zorgen we ervoor dat er geen dubbelingen ontstaan van tools die exact hetzelfde probleem oplossen maar volledig los van elkaar worden ontwikkeld met overheidsgeld. Deels verspilling maar ik denk ook deels nodig in deze fase van de hype waar vergaande centralisatie van ontwikkeling zonder echt exact duidelijk te hebben wat er ontwikkeld dient te worden alleen tot bureaucratisering en vertraging van het ontwikkelproces leidt. Hoe bouw je bruggen tussen 1600 organisaties zonder ontiegelijke vertraging in communicatie en executiekracht? 

Er gebeurt genoeg en het zal interessant zijn waar bepaalde tools over een jaar staan; denk bijvoorbeeld aan [vlam.ai](vlam.ai) die in 2026 alle 100.000 ambtenaren willen bedienen met Vlam-chat. Als dit succesvol is; zou dit dan alle andere generieke chat oplossingen bij de diverse uitvoeringspartijen overbodig maken? Ik vraag me vooral ook af of de schaal en snelheid er is qua GPUs en de moeilijkheid qua stroomuitbreidingen voor de overheidsdatacenters. Of toch meer publiek-private samenwerking om bestaande datacenter capaciteit in te huren zolang deze in overheidscentra nog niet gefaciliteerd kan worden door de bestaande harde IT overheidsclubs. 

You’re absolutely right dat het een interessant jaar kan gaan worden. 
