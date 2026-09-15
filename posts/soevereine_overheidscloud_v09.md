---
title: soevereine overheidscloud v0.9
date: 2026-09-15
description: wat vertelt versie 0.9 van de soevereine overheidscloud ons over de aanpak van deze nieuwe cloud?
---

Het ontwerp voor de Soevereine Overheidscloud is op versie 0.9 beland. 
Het is mooi om te zien dat Gartner direct al in de inleiding wordt genoemd; Gartner blijft toch diehard een plekje houden in de managementlagen. 

Uit het ontwerp en de stukken daaromheen zijn wel wat interessante zaken te halen over de toekomstige rijkscloud die zou moeten gaan ontstaan. 
Het eerste punt is daarbij de insteek voor een containerplatform, wat denk ik erg fijn en modern is. 
Wat daar verder nog bijkomt is dat het inzet op de Cloud Native Computing (CNCF) onderdelen wat wil zeggen dat er wordt ingezet op een groot Kubernetes platform of cloud. 

Een ander interessant punt is dat er niet gekozen wordt om de reeds bestaande overheids Kubernetes cloudplatformen te koppelen of te pushen op het samengaan naar 1 groot overheids kubernetes platform. 
Nee, er wordt gekozen voor nieuwbouw naast de bestaande overheids "clouds". 
Dat kan natuurlijk voordelen hebben door aan het begin gelijk goede keuzes te maken, maar het is dan ook de vraag waar deze nieuwe cloud mag landen. Is dat bij een bestaande overheids IT dienstverlener die reeds een Kubernetes cloud aanbod heeft? 
Of wordt er stiekem toch ingezet op nog een nieuwe overheids IT dienstverlener. 

Verder wordt er bewust voor SEAL-4 (voor software) gekozen met dus de meest vergaande soevereiniteitssopties die de EU Cloud Sovereignty Framework (EUCSF) biedt. 
Wel wordt bewust gekozen om het platform niet geschikt te maken voor Hoog Gerubriceerde Informatie. 
Het platform zal dus geen vervanging zijn van de bestaande omgevingen die voor staatsgeheimen geschikt zijn. 
Opzich best logisch als je het pakket van eisen ziet wat daaraan hangt, maar het zorgt er ook voor dat je niet direct een bepaalde groep applicaties binnen kan halen die verplicht on premise uitgevoerd moeten worden. 
Blijft natuurlijk wel de vraag of je met deze speciale applicaties/data naar een cloud zou willen verhuizen die zo nieuw is.. misschien toch eerst een aantal jaren uitwachten. 

Ook wordt er rekening gehouden met "open source first" wat ook heel logisch is en ik ben benieuwd hoe bepaalde pijnpunten in de inrichting worden aangepakt als er geen opensource tool beschikbaar is. 
Gaat de overheid dan ontwikkelaars subsidiëren zoals bijvoorbeeld voor een tool als Garage is gebeurt? 
Of zijn enterprise tooling die qua licentie niet open source zijn maar wel open code dan toch ook opeens "open source"? 
Realistisch kan je denk ik ook niet alles in 1x 100% open neerzetten als je daarbij ook nog een realistisch tijdspad wilt hebben om daadwerkelijk een cloud live te hebben binnen afzienbare tijd. 
Het zou wel goed zijn technical debt te beschrijven en die dan op langere termijn uit te faseren voor alternatieven. 

Grote hamvraag is nog wel van het Leveringsmodel gaat zijn voor de nieuwe cloud; wordt dit wederom een prachtig offertetraject met allemaal interne accountmanagers en levertijden in maanden.. of P*Q en een opentofu statement die je wat laat uitrollen na RijksSSO? 
Dit lijkt iets voor V2 van de uitwerking te zijn. 
Ook de precieze funding blijft lastig zolang er geen pot geld vanuit het rijk komt. 
Wie gaat de grote investeringsinspanningen dragen voor een nieuwe cloud? 

Qua scoping wordt het platform primair ook ingezet op applicatiehosting als eerste doel met opties om later uit te breiden naar PaaS/SaaS of data diensten. 
Voorlopig zullen de data teams dus nog steeds hun heil moeten zoeken bij de public cloud diensten en de specifieke diensten die de bestaande IT dienstleveranciers voorzien. 

Wat verder ook nog een heel mooi punt is dat de insteek is dat iedere overheidorganisatie gebruik moet kunnen maken van de cloud. 
Klinkt niet gek, maar is in praktijk voor veel overheidsclouds wel het geval. 
Ben jij een kleine gemeente of een ZBO onder het verkeerde ministerie? 
Dan kan het zijn dat je niet gebruik mag maken van een platform wat gewoon up en running is bij een bestaande overheids IT dienstverlener omdat ze je niet willen servicen. 

Nu wordt het interessantste; welk overheidsonderdeel gaat dit dragen en de MVP realiseren? Hoe lang blijft dit nog in de documentfase hangen? 

Zie het publieke [NDS document](https://pgdi.nl/file/download/ab69c431-9177-446e-a154-d557fc3b7eb9/NDS_Overheidsbrede_Soevereine_Clouddienst_Ontwerp_v0.9.pdf)
