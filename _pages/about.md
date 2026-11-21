---
permalink: /
title: "About"
excerpt: "About"
hide_title: true
home: true
redirect_from: 
  - /about/
  - /about.html
---
Hi! I'm a computational physicist with experience in end-to-end research and AI pipelines: hardware, data engineering, data science and agentic AI.

I have experience as both researcher and technical backbone for multiple research labs, building complex backend infrastructure and directing the computational aspects of research. From my academic career, I have extensive expertise analysing social media platforms at scale, learning what makes them tick.

<div class="sec">Current work</div>
<div class="pcards">
{%- for p in site.data.projects.featured %}
  <div class="pc">{% if p.docs %}<a class="go" href="{{ p.docs }}">docs →</a>{% endif %}<a class="stretch" href="https://github.com/{{ p.repo }}"><b>{{ p.name }}</b></a><div class="x">{{ p.description }}</div><div>{% for t in p.topics %}<span class="chip">{{ t }}</span>{% endfor %}</div></div>
{%- endfor %}
</div>

<div class="sec">Selected publications</div>
<div class="pubs">
{%- assign selected = site.data.publications | where: "selected", true -%}
{%- for p in selected %}{% include pub.html pub=p show_year=true %}{% endfor %}
</div>

<p class="more"><a href="{{ '/research/' | relative_url }}">All research →</a></p>
