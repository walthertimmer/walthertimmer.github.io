---
title: serverless cloudflare cloud
date: 2026-01-16
description: Gedachtes over een open source data platform. Hoe kan dit eruit zien? Welke tooling komt erbij kijken? En waar moet je aan denken?
---

# Serverless Cloudflare cloud

De kerstvakantie is altijd een goede periode om wat te hobby'en naast alle dagen gevuld met sociale familie activiteiten. (Plus ook een goed moment om de laatste griep mee te pakken..)

Naast de grote 3 clouds (AWS/Gcloud/Azure) is er ook nog een hele grote 'edge' cloud die circa ±20% van het internetverkeer verwerkt; Cloudflare. Eerder had Cloudflare vooral de beste DDOS protectie die vooral voor grotere websites en instellingen interessant is. En een hele hoop gamingservers. Dit samen met DNS was min of meer de core business van Cloudflare met riante gratis credits voor kleine sites en MKB. En af en toe riante enterprise contracten om deze gratis credits terug te verdienen als je Reddit mag geloven. Puur op financials is Cloudflare onderhand een [bedrijf](https://stockanalysis.com/stocks/net/revenue/) met ongeveer 2 miljard aan omzet en ook steeds meer funding om buiten de networking/DDOS hoek functionalitieit te ontwikkelen. 

Bij een bepaalde schaal gaan netwerkkosten steeds vaker 1 van de core componenten van je cloud bill zijn en speelt dit soms zwaarder dan de compute of storage kosten die je dient af te tikken. Dit is vooral het geval bij applicaties en services gericht op diensten aanbieden naar buiten (het internet) en niet perse in je eigen private vnet waar je deze kosten niet voelt... tot je meerdere cloud locaties dient te gebruiken omdat er een GPU shortage is in bepaalde zones. Extra interessant is dan dat Cloudflare geen egress costs hanteert wat een erg groot verschil kan maken qua kosten.

Enfin Cloudflare timmert hard aan de weg met Cloudflare Pages (voor statische sites met wat functies on the side) en Cloudflare Workers (dynamische websites) met daarbij nog ondersteunende diensten zoals een managed Sqlite oplossing (D1), Hyperdrive voor de traditionele sql backends en R2 als S3 storage. Deze laatste bevat nu ook een managed iceberg catalog wat het gebruik van deze storage als data lake een stuk makkelijker maakt. Ook is er nu in beta de mogelijkheid om 'serverless' containers te draaien in combinatie met Cloudflare workers wat de mogelijkheden qua applicaties die je kan draaien weer een stuk groter maakt (of wellicht zelfs alle bestaande limieten van Workers oplost). 

Met serverless functies en de ondersteuning van diverse [AI modellen](https://developers.cloudflare.com/workers-ai/models/) is op data vlak al best veel mogelijk qua AI applicatie die je serverless wilt bouwen zonder na te hoeven denken over schaalscenario's en het management van diverse modellen. Uiteraard moet Cloudflare wel voldoen aan je interne beleid maar als je kijkt wat voor tools je neer kunt zetten en tegen welke effectieve prijzen door de best fanatieke pricing strategie ten opzichte van de grote clouds is het een interessant platform. 

Effectief is de grootste moeilijkheid in Cloudflare wellicht nog wel het succes van Cloudflare zelf. Cloudflare is zo erg gefocused op applicaties en websites die wereldwijd beschikbaar moeten zijn en snel moeten zijn dat er qua ontwikkeling en focus niet altijd direct wat bij zit voor een intern gerichte applicatie of tool. Effectief zul je dan vaak ook niet de schaal nodig hebben die Cloudflare je biedt maar zeker wel de interessante pricing die serverless Cloudflare je biedt ten opzichte van de grotere wolken. Flows neerzetten die expliciet intern moeten blijven in je bedrijfsnetwerk, ook bij issues en bugs, zijn lastiger (of bij sommige diensten onmogelijk) neer te zetten. Het is ook de vraag of het voor een Cloudflare goed is om ook deze mogelijkheden verder te gaan ontwikkelen of juist de extreme focus op schaal altijd als prioriteit in het ontwikkelen mee te nemen. Veel clouds bieden natuurlijk veel services aan die niet best in class zijn maar simpelweg aantrekkelijk omdat je toch ook al die andere 100+ services daar afnam. Net een supermarkt. 

Verder blijft de openheid over issues in de blogs van Cloudflare altijd erg mooi, vooral tov de summierheid en NDAs van andere partijen. 

## Dublin in ectasy

<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/_OOrjMjeUqg?si=Wi1Wtrdf3RMQLRCX&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
