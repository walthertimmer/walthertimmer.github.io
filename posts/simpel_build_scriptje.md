---
title: Simpel build scriptje
date: 1994-06-07
description: Hoe je een eenvoudig Python build script maakt om markdown bestanden om te zetten naar HTML voor je blog zonder externe dependencies.
---

# Simpel build scriptje

Om gemakkelijk wat blogposts te maken is het fijn om in markdown te kunnen werken. Er zijn diverse tools die dit op telefoon etc aanbieden zonder veel gedoe. Een website direct in html en css bouwen heeft zo haar charme maar wordt op een gegeven moment ook wat **irritant** als je voornamelijk  mobiel (lees kleine schermpjes) werkt.

## Mogelijkheden met een simpel build scriptje

- Headers (H1, H2, H3)
- **Bold text** and *italic text*
- `inline code` and code blocks
- [Mooiste website ooit](https://walthertimmer.nl)
- Prachtige lijstjes zoals deze!

## Voorbeeldcode

```python
def hello_world():
    print("Hello from markdown!")
```

# Plaatjes

Worden dan ook plaatjes netjes omgezet? Ja, zie hieronder:

![Random architectuur plaatje](../images/modern-data-analytics-on-aws.png)

## Conclusie

Bovenstaande opties maken het allemaal een stuk fijner om even wat in markdown neer te pennen. Bovendien vermijdt je met een simpel build scriptje Jekyll en aanverwanten die in mijn ervaring toch ook weer van erg veel dependencies samenhingen. Of weer teveel configuratie of te weinig html vrijheid om mijn website zo lelijk mogelijk te maken.
