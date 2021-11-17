---
layout: post
title:  "New year new site!"
date:   2021-11-17 10:52:00 +0100
categories: blog tech
---

Occasionally I like to rebuild my personal site to play with new tech stacks. 15+ Years ago WordPress always seemed to be the default for a smaller easy to use website. Easily extendible with plugins and even custom themes. Just spin up a low-cost VM with a Linux distro and you’re set.  

Nowadays with the content delivery networks (CDN) it seems to be interesting to create static sites that can cheaply and safely be hosted at every large cloud provider. However you still want to be able to easily make new posts and pages and deploy them to your website. Jekyll steps into that void. 

Jekyll offers easy edits of posts and pages through markdown and automatically generates a static website which can be deployed on every CDN. 

One can easily adjusts and test new additions locally on a VM or laptop and when satisfied check-in these changes to GIT(hub). GitHub Actions can then automatically build and deploy the latest GIT commit to a CDN.
 
