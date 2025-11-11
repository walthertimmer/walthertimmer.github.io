---
title: Infrastructure as Code & Pulumi
date: 2025-11-03
description: Wat brengt Pulumi wat Infrastructure as Code nog nodig had?
---

# Infrastructure as Code & Pulumi

Infrastructure as Code (IaC) is al een paar jaar gemeengoed.
Daarmee werd veelal de lokale SDK van een cloud provider bedoeld om een en ander qua configuratie gemakkelijk uit te rollen.
Of de one tool to rule them all; Terraform.
De grote verscheidenheid aan providers in het Terraform landschap zorgt er eigenlijk voor dat je deze tool voor praktisch alles in kan zetten en dat de tool erg dominant is geworden.

## State

Enigste issue van Terraform is natuurlijk dat het, in tegenstelling tot OpenTofu, niet in staat is om state en variables te encrypten. Niet omdat dat zo moeilijk is, maar meer omdat de een van de primairste redenen is om als enterprise een goed contract af te sluiten voor het opslaan van je state. Gierig zijn en je state in een storage container opslaan terwijl al je variabelen en state unencrypted is blijft een veel te groot risico.
Vooral als je niet alleen simpele cloud config opslaat maar ook connecties tussen systemen. In de ideale wereld zou dit allemaal via IAM gaan en zou er geen issue zijn.
In de echte wereld eindig je dan toch vaak met wachtwoorden in een onveilige state.
Het mooie daarvan is natuurlijk dat je zaken als Azure Keyvault hebt om dit op te lossen maar ook als je deze gebruikt wil Terraform data opslaan in haar state, die je helemaal niet op wilt slaan. Bijna alsof de ontwikkelaars van Terraform weten wat hun verdienmodel is.
Issue is alleen dat je als je contractueel met Terraform in zee gaat je deze partij erg goed moet vertrouwen en dit beleidsmatig erdoorheen moet kunnen krijgen.
Idealiter hou je je holy grail qua config en secrets dicht bij je en deel je deze met zo min mogelijk partijen.

Nu kan je dus hiervoor de OpenTofu route opgaan maar je kan ook kijken naar de nieuwe aanpak via Pulumi.
Terraform/OpenTofu YAML files zijn natuurlijk erg sexy om te bewerken en bij te houden.
Helemaal als je hier diverse modules voor dient te maken en je steeds verder gaande automatisering en dynamisering van je code wilt doorvoeren.
Op enig moment kom je dan op het punt dat je afvraagt waarom je in een YAML file iets aan het ontwikkelen bent wat in menig ander normale programmeertaal allang standaard is en geen custom logica en keuzes vereist.
Hence Pulumi.

## Pulumi

Het gave van Pulumi is dat je in diverse programmeertalen (kies de gene waar je je het prettigst bij voelt) je infrastructuur kunt vastleggen.
Waarom zou je je hele applicatie in code x programmeren om vervolgens infrastructuur in YAML te bewerken?
Cloud of on-prem (mits juiste provider) infrastructuur kunnen vastleggen en de deployments op Kubernetes op deze manier inregelen zijn erg waardevol en verkleinen de gap voor software engineers.
En vooral bij het verder dynamisch maken van setups indien je infrastructuur inregelt voor niet alleen je eigen app of team maar het dient regelen voor de gehele organisatie en dus tig omgevingen wilt neerzetten kan Pulumi echt meerwaarde bieden.

Pulumi werkt ook met providers en deelt daarmee eigenlijk ook hetzelfde minpunt als de Terraform broertjes; deze lopen altijd ietwat achter de APIs die diverse tools bieden.
Geen probleem als je breed gebruikte tooling inzet maar veelal heb je net die ene CLI command nodig om toch nog iets in te regelen.
Als dit via je favoriete programmeertaal kan is dat toch net wat prettiger en consequenter in aanpak dan een los powershell of bash script wat ertussen wordt gefrommeld.
Vooral omdat veelal de IAM sync en koppeling toepassingen en encryptie toepassingen net weer unstable blijken te zijn in een provider.

En het mooiste is dat [Pulumi](https://github.com/pulumi/pulumi) Apache 2 hanteert en daarom geen onduidelijkheden biedt wat betreft het professioneel inzetten.
Plus wel default encryptie van variabelen in je state indien je er toch iets in beland wat je idealiter niet breed deelt.

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/9PqbCv3F_8c?si=Q-rNy7rhqsm8ZWV6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>
