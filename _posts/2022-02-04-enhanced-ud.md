---
layout: post
title: Enhanced Universal Dependencies
categories: [Dependencies, Syntax]
---

<!--- Main URL: add exactly one link here, replacing only the URL --->
[Link to Annotation Guidelines](https://universaldependencies.org/u/overview/enhanced-syntax.html)

<!--- Languages -->
* English
* tba

<!-- Teaser image, delete next line if none -->
![](http://sigann.github.io/guido/images/2022-02-04-enhanced-ud.png)

<!-- Description -->
# Description
*Taken from the Enhanced UD website (see link above):*
We always intended the Universal Dependencies representation to be used in shallow natural language understanding tasks such as relation extraction or biomedical event extraction. For such tasks, one is typically interested in the relation between certain entities, e.g., the relation between two persons or whether one protein interacts with another. UD is particularly well suited for such tasks as UD trees contain many direct dependencies between content words and many of the dependency labels provide a lot of information about the type of relation between two content words. However, for some constructions, the dependency path between two content words of interest can be very long in a UD tree, which complicates determining how the content words are related. Further, some dependency types such as obl or nmod are used for many different types of arguments and modifiers, and therefore they are not very informative on their own. For these reasons, we also provide guidelines for an enhanced representation, which makes some of the implicit relations between words more explicit, and augments some of the dependency labels to facilitate the disambiguation of types of arguments and modifiers.


<!-- Domains and Genres -->
# Domains and Genres
* various

<!-- Any further references, links etc. -->
# References
Sebastian Schuster and Christopher D. Manning. [Enhanced English Universal Dependencies: An Improved Representation for Natural Language Understanding Tasks](https://aclanthology.org/L16-1376/). 2016.
