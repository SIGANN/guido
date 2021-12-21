---
layout: page
permalink: /categories/
title: Categories
---

*TODO*
* display category icons with anchors
* if page gets too large, we need sub-pages for the individual topics, with search + browsing in the individual topics (but let's start with this and see how long it is sufficient - maybe we'll need to add a database at some point, but I am not sure at this point if there really are this many guidelines in NLP that this wouldn't scale any more)
* make display of results more concise, e.g., left-aligh

<div id="archives">
{% for category in site.categories %}
  <div class="archive-group">
    {% capture category_name %}{{ category | first }}{% endcapture %}
    <div id="#{{ category_name | slugize }}"></div>
    <p></p>
    
    <h3 class="category-head">{{ category_name }}</h3>
    <a name="{{ category_name | slugize }}"></a>
    {% for post in site.categories[category_name] %}
    <article class="archive-item">
      <h4><a href="{{ site.baseurl }}{{ post.url }}">{% if post.title and post.title != "" %}{{post.title}}{% else %}{{post.excerpt |strip_html}}{%endif%}</a></h4>
    </article>
    {% endfor %}
  </div>
{% endfor %}
</div>
