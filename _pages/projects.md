---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

{% assign sorted_projects = site.projects | sort: "order" %}
{% for post in sorted_projects %}
  {% include archive-single-research.html %}
{% endfor %}
