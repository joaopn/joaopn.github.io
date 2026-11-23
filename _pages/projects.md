---
title: "Projects"
permalink: /projects/
wide: true
redirect_from:
  - /software/
  - /projects/sdp/
  - /projects/agentic-dev-sandbox/
---
{%- assign pr = site.data.projects -%}
{% for p in pr.featured %}{% include project-card.html project=p %}{% endfor %}

<div class="rows">
{%- for p in pr.list %}
  <div class="rw"><div><a class="repo stretch" href="https://github.com/{{ p.repo }}">{{ p.repo }}</a><div class="x">{{ p.description }}</div></div>{% if p.docs %}<span class="btns"><a class="btn pri" href="{{ p.docs }}">Docs</a></span>{% endif %}</div>
{%- endfor %}
</div>

<div class="sec">Models</div>

{{ pr.models.intro | markdownify }}

<div class="models">
  <ul>{% for m in pr.models.items %}<li>{{ m }}</li>{% endfor %}</ul>
  <a class="btn" href="{{ pr.models.collection }}">Hugging Face collection ↗</a>
</div>
