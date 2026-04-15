---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% assign sorted_research = site.research | where_exp: "post", "post.title != 'Other projects'" | sort: "order" %}
{% for post in sorted_research %}
  {% include archive-single-research.html %}
{% endfor %}

{% for post in site.research %}
  {% if post.title == "Other projects" %}
    {% include archive-single-research.html %}
  {% endif %}
{% endfor %}
