---
title: nederlandse trainingsdata
date: 2026-10-26
description: hoeveel potentie is er voor Nederlandse trainingsdata voor AI en LLMs?
---

# Nederlandse trainingsdata

Na een lange lege periode met alleen maar kleinere Europese AI labs die Chinese distillen en relabellen als “Europese” AI zijn er opeens weer 2 nieuwe modellen die er wel toe doen. 

Mistral die met large 4 komt, aka Le Chonk, en het Duitse Aleph Alpha met haar tweede model, Kolibri. 
Niet geheel verrassend is Kolibri niet alleen goed in Engels maar juist ook in het werken in het Duits door o.a. >20% trainingsmateriaal in het Duits. 
Dat zorgt er eigenlijk ook voor dat het interessant zou zijn om zo'n zelfde trainingpipeline te draaien voor de uitkomst van GPTNL; oftewel de verzamelde bak oernederlandse trainingsdata. 
In totaal gaat het om ±4.3T aan pre-training tokens in het Duits. 

Een stapje groter dan het 78.1B Kolibri model is Large 4 met ±1000B parameters wat ervoor zorgt dat er in verschillende groottes wat te kiezen is. 
Vermoedelijk komen in het najaar/begin van 2027 de eerste kleinere modellen van Mistral op basis van Large 4. 

Wat wel interessant is aan het Europese AI nieuws is dat de Duitse variant met 268 Nvidia Blackwell GPUs is getraind en de Franse variant met 3800 Nvidia Blackwell GPUs. 
Aantallen die niet geheel schokkend zijn in de huidige wereld waar moderne datacenters zoals bijvoorbeeld die van xAI al boven de 500.000 GPUs zitten. 
Dat laat ook zien dat je met ±10 miljoen euro aan infra en een goed team in een jaar een leuk model kan neerzetten. Natuurlijk niet op alle vlakken net zo cutting edge als de frontier modellen, wat voor een groot deel zal zitten in het verschil aan beschikbare goede trainingsdata. 
Maar het maakt het wel interessant om te zien waar Europa precies mee komt op het vlak van subsidies en initiatieven voor Europese AI. 
Een eigen model trainen hoeft dus niet zo moeilijk te zijn in praktijk. 
Het zal vooral de harde voorsprong zijn van interference mogelijkheden om de modellen breed aan te bieden en het grote voordeel dat Amerikaanse en Chinese partijen hebben om nu al grootschalige trainingsdata te verzamelen van alle gebruikers van de modellen. 
Zo blijft data het nieuwe goud , of de nieuwe olie. 

Daarmee blijft het jammer dat de [publieke dataset voor GPT-NL](https://huggingface.co/datasets/GPT-NL/GPT-NL_Public_Corpus) eigenlijk maar 36 miljard tokens aan Nederlands input bevat. 
Mis je toch een factor ±119 voor een Nederlandse Kolibri. 
De vraag is ook hoeveel je zou kunnen verzamelen aan Nederlandse trainingsdata als je juist ook niet publieke data zoals alle boeken, tijdschriften en kranten mee zou pakken voor een nieuwe trainingsset. 
Misschien toch nog tijd voor een tweede ronde van een [RVO/EZK subsidie](https://www.rtl.nl/nieuws/rtl-z/artikel/5416834/tno-gpt-nl-nederlandse-chatgpt-ai) van 13.5 miljoen om dit tewerk te stelligen. Ik ben benieuwd hoeveel trainingsdata je kunt verzamelen door alle overheidsarchieven van de ±1400 overheidspartijen samen te gooien met alle Nederlandse kranten en boeken die standaard ook al gedigitaliseerd worden maar nog onder een restrictieve licentie vallen. 

Gegeven dat er in 1993 ±34000 boeken in Nederland zijn gepubliceerd (bron UNESCO) en Delpher circa 200.000 historische boeken bevat. 
Als je dan rekent met 30.000 boeken per jaar sinds het jaar 2000 kom je uit op bijna een miljoen (980k) unieke boeken wat best wel kan kloppen als we zien dat de Nederlandse bibliotheken gezamenlijk iets meer dan 20 miljoen boeken hebben. 
Er zullen een hoop dubbele zijn om uit te lenen. 
Als je dan rekent met 100.000 tokens per boek waarbij je enigszins conservatief zit kom je uit op een totaal van 98 miljard tokens wat meer dan een verdubbeling is aan tokens van GPT-NL. 
Tel daarbij dan nog alle andere publicaties zoals tijdschriften, kranten en andere media dan is er nog potentie voor veel groei in de Nederlandse trainingsdata en daarmee ook de groei van kwaliteit van LLMs in het Nederlands. Misschien een leuke toevoeging voor de archiefwet; verplichte toevoeging aan de trainingsset na zoveel jaar. 
Trainingsdata as a service (TaaS). 

- [Kolibiri persbericht](https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/)
- [Kolibri docs](https://aleph-alpha.com/downloads/tech-report.pdf)
- [Mistral Large 4 persbericht](https://mistral.ai/news/mistral-large-4/)
- [Mistral Large 4 docs](https://docs.mistral.ai/models/mistral-large-4-0)
