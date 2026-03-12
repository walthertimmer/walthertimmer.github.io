---
title: domeinmigraties
date: 2026-03-13
description: Domeinmigraties en een simpele setup voor wat statische websites
---

# domeinmigraties

Nadat SIDN al die [moeite](https://www.sidn.nl/nieuws-en-blogs/het-waarom-achter-onze-keuze-voor-public-cloud-en-aws) [doet](https://www.rijksoverheid.nl/documenten/kamerstukken/2025/01/17/kamerbrief-besluit-sidn-migratie-nl-domeinregistratiesysteem-naar-aws) [om](https://www.dutchitleaders.nl/news/460755/aivd-onderzoekt-mogelijke-risicos-bij-verhuizing-sidn-naar-aws) [een](https://www.security.nl/posting/872841/SIDN+mag+registratiesysteem+van+kabinet+deels+naar+Amazon+verhuizen) [registratiesysteem](https://www.techzine.nl/nieuws/privacy-compliance/562576/sidn-migratie-naar-aws-gaat-door-ondanks-geopolitieke-spanningen/) [naar](https://www.computable.nl/2025/01/17/kabinet-stelt-beperking-aan-verhuizing-sidn-systeem-naar-aws/) AWS te krijgen leek het mij goed om voor een aantal websites die ik had weer eens de boel naar 1 partij te migreren.
Zo had ik altijd het gros van mijn domeinen bij AWS geregistreerd staan omdat die al (naar mijn idee) 10 jaar min of meer dezelfde prijzen rekenen zonder de jaarlijkse prijsverhogingen van tientallen procenten die sommige Nederlandse hosters hanteren.
Nu lijkt daar met mijn.host als relatief nieuwe partij verandering en transparantie in te zijn gekomen dus dat moet je dan belonen. 
Helemaal aangezien mijn.host voor verhuizingen geen geld rekend. 

Daarnaast lijkt Cloudflare ook het besluit genomen te hebben om zowel beschermheer des websites als ook [scraper des websites](https://developers.cloudflare.com/changelog/post/2026-03-10-br-crawl-endpoint/) te worden.
Dat betekend ook dat er of een bunny.net of een reverse proxy voor gezet moet worden voor mijn veelal simpele statische websites. 

De effectieve setup valt in onderstaand plaatje te zien. Met eleventy worden websites gegenereerd die uit een PostgreSQL dynamische data halen.
Met CI/CD pipelines die periodiek draaien en dus de statische websites vernieuwen maakt het mogelijk om simpele niet hackbare websites te hebben die belachelijk veel load aan kunnen in de huidige setup.
Data van websites landt op objectstorage en kan vanaf daar door Nginx worden voorgeschoteld met wel een caching laag ertussen zodat er niet telkens netwerk calls nodig zijn. 
Voor websites die gericht zijn op de Nederlandse markt is dat meer dan voldoende, helemaal met de hardware van tegenwoordig. 

Het hele GIT en CI/CD verhaal blijft voorlopig wel Amerikaans aangezien het duopolie Gitlab en GitHub daar geen andere Europese competitie hebben.
Het enigste wat er nu is, is Codeberg maar dat is nadrukkelijk niet commercieel inzetbaar. 

Verder heb ik ook websites bij bunny.net staan maar weer een losse partij erbij is ook niet gewenst. KISS & less is more.
Ook de cloud native oplossingen zoals Edge services binnen Scaleway lijken relatief simpele maar toch essentiële zaken (denk aan bepaalde redirects/page rules) nog niet te ondersteunen.

Van Google PageSpeed krijgen de websites weer een score van 100 qua performance dus ik ben tevreden.

![websites](../images/websites.drawio.svg)
                                                                                                                               
