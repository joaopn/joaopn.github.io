---
title: "Personal"
permalink: /personal/
redirect_from:
  - /year-archive/
  - /tags/
  - /categories/
  - /wordpress/blog-posts/
---
<div class="posts">
{%- for post in site.posts %}
  <div class="post"><span class="d">{{ post.date | date: "%b %Y" }}</span><div><a class="stretch" href="{{ post.url | relative_url }}"><b>{{ post.title }}</b></a><span class="r">{% include read-time.html content=post.content %}</span></div></div>
{%- endfor %}
</div>
