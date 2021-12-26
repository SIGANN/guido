---
layout: page
title: Search
permalink: /search/
---

<div id="search-container">
    <input type="text" id="search-input" placeholder="Search through the annotation guidelines entries...">
    <ul id="results-container"></ul>
</div>

<script src="{{ site.baseurl }}/assets/simple-jekyll-search.min.js" type="text/javascript"></script>

*TODO*

* make display of search results more concise?
* display hits in alphabetical instead of temporal order (yet for the posts the date numbering might not be bad because it lets us keep track of when things have been added etc. and give the page a feel of being up to date on the landing page)

<script>
    SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    searchResultTemplate: '<div style="text-align: left !important;"><a href="{url}"><h1 style="text-align:left !important;">{title}</h1></a></div>',
    json: '{{ site.baseurl }}/search.json'
    });
</script>
