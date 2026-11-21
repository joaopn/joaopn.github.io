---
title: "Research"
permalink: /research/
wide: true
redirect_from:
  - /teaching/
  - /teaching/2023-network-science/
  - /teaching/2024-social-networks/
  - /teaching/2025-KI-MC/
  - /teaching/2025-arqus-summer-school/
  - /projects/social-media-research/
  - /publications/
  - /publications/2017-inhibition-rtn
  - /publications/2018-review-reverberating
  - /publications/2019-critical-avalanches
  - /publications/2020-covid19-forecast
  - /publications/2020-mrestimator
---
{%- assign pubs = site.data.publications -%}
{%- assign cards = site.research | sort: "order" -%}
{%- assign areas = site.areas | sort: "order" -%}
<div class="toc"><a href="#areas">Areas</a><a href="#publications">Publications</a><a href="#teaching">Teaching</a></div>

<div class="acards" id="areas">
{%- for card in cards %}
  {%- assign n_pap = 0 -%}{%- assign n_th = 0 -%}{%- assign y0 = 9999 -%}{%- assign y1 = 0 -%}
  {%- for p in pubs -%}
    {%- if card.areas contains p.area -%}
      {%- if p.thesis %}{% assign n_th = n_th | plus: 1 %}{% else %}{% assign n_pap = n_pap | plus: 1 %}{% endif -%}
      {%- if p.year < y0 %}{% assign y0 = p.year %}{% endif -%}
      {%- if p.year > y1 %}{% assign y1 = p.year %}{% endif -%}
    {%- endif -%}
  {%- endfor %}
  <button type="button" class="ac" id="{{ card.slug }}" data-f="{{ card.areas | join: ' ' }}" aria-pressed="false">
    <b>{{ card.title }}</b>
    <span class="x">{{ card.excerpt | markdownify | remove: '<p>' | remove: '</p>' | strip }}</span>
    <span class="c">{{ n_pap }} paper{% if n_pap != 1 %}s{% endif %}{% if n_th > 0 %} · {{ n_th }} thes{% if n_th == 1 %}is{% else %}es{% endif %}{% endif %}{% if y1 > 0 %} · {% if y0 == y1 %}{{ y0 }}{% else %}{{ y0 }}–{{ y1 }}{% endif %}{% endif %}</span>
  </button>
  {%- assign intro = card.content | strip -%}
  {%- if intro != "" %}<template data-t="intro-{{ card.slug }}">{{ card.content | markdownify }}</template>{% endif %}
{%- endfor %}
</div>

<div class="sec" id="publications">Publications</div>
<div class="filters" id="pf">
  <button type="button" data-f="all" class="on">All</button>
  {%- for a in areas %}<button type="button" data-f="{{ a.key }}">{{ a.label }}</button>{% endfor %}
  <button type="button" data-f="th">Theses</button>
</div>
<div class="abox" id="ab" hidden><div class="abh"><b id="abt"></b><button type="button" class="aclose" id="abx" aria-label="Close">×</button></div><div id="abc"></div></div>
{%- for a in areas %}
<template data-t="{{ a.key }}">{{ a.content | markdownify }}</template>
{%- endfor %}
<div class="fstate" id="fs" aria-live="polite"></div>
<div class="publist" id="pl">
{%- assign by_year = pubs | group_by: "year" -%}
{%- for y in by_year %}
  <div class="yr" data-y>{{ y.name }}</div>
  {%- for p in y.items %}{% include pub.html pub=p tags=true %}{% endfor %}
{%- endfor %}
</div>

<div class="sec" id="teaching">Teaching</div>
<div class="teach">
{%- assign teaching = site.teaching | sort: "date" | reverse -%}
{%- for t in teaching %}
  <span class="s">{{ t.season }}</span><div class="w">{% if t.description %}{{ t.description }} - {% endif %}{% if t.paperurl %}<a href="{{ t.paperurl }}">{{ t.title }}</a>{% else %}{{ t.title }}{% endif %} <i>— {{ t.venue }}</i></div>
{%- endfor %}
</div>

<script src="{{ '/assets/js/research.js' | relative_url }}" defer></script>
