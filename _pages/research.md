---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% assign sorted_research = site.research | sort: "order" %}
{% for post in sorted_research %}
  {% include archive-single-research.html %}
{% endfor %}

<h1 id="teaching" style="margin-top: 1.5em;">Teaching</h1>

<div class="textbox textbox--static">
{% assign grouped_posts = site.teaching | group_by: 'season' | sort: 'name' | reverse %}
{% for group in grouped_posts %}
  <h2>{{ group.name }}</h2>
  <ul>
  {% for post in group.items reversed %}
    <li>
      {% if post.description %}{{ post.description }} - {% endif %}{% if post.paperurl %}<a href="{{ post.paperurl }}">{{ post.title }}</a>{% else %}{{ post.title }}{% endif %} &mdash; <em>{{ post.venue }}</em>
    </li>
  {% endfor %}
  </ul>
{% endfor %}
</div>
