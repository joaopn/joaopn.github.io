---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% assign grouped_posts = site.teaching | group_by: 'season' | sort: 'name' | reverse %}

{% for group in grouped_posts %}
  <h2>{{ group.name }}</h2>
  {% for post in group.items reversed %}
    {% include archive-single-teaching.html %}
  {% endfor %}
{% endfor %}
