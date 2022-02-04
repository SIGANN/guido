---
layout: post
title: SOFC-Exp Corpus
categories: [Named Entities, Event Extraction, Semantic Role Labeling]
---

<!--- Main URL: add exactly one link here, replacing only the URL --->
<!--- more links only if absolutely necessary, e.g., if there are several languages and you do not see a point of adding another page. -->
[Link to Annotation Guidelines](https://github.com/boschresearch/sofc-exp_textmining_resources)

<!--- Languages adressed -->
* English

<!-- Teaser image, delete next line if none -->
![](http://sigann.github.io/guido/images/sofc-exp-corpus.png)

<!-- Description -->
# Description
The SOFC-Exp corpus contains 45 scientific publications about solid oxide fuel cells (SOFCs), published between 2013 and 2019 as open-access articles all with a CC-BY license. Materials science domain experts used INCEpTION to manually annotate the dataset the following information:

* Mentions of relevant experiments have been marked using a graph structure corresponding to instances of an Experiment frame. We assume that an Experiment frame is introduced to the discourse by mentions of words such as report, test or measure (also called the frame-evoking elements). The nodes corresponding to the respective tokens are the heads of the graphs representing the Experiment frame.
* The Experiment frame related to SOFC-Experiments defines a set of 16 possible participant slots. Participants are annotated as dependents of links between the frame-evoking element and the participant node.
* In addition, we provide coarse-grained entity/concept types for all frame participants, i.e, MATERIAL, VALUE or DEVICE. Note that this annotation has not been performed on the full texts but only on sentences containing information about relevant experiments, and a few sentences in addition. In the paper, we run experiments for both tasks only on the set of sentences marked as experiment-describing in the gold standard, which is admittedly a slightly simplified setting. Entity types are only partially annotated on other sentences. Slot filling could of course also be evaluated in a fully automatic setting with automatic experiment sentence detection as a first step.

The dataset, along with detailed annotation guidelines, is publicly available in a custom stand-off format (similar to Brat) under CC-BY at [GitHub](https://github.com/boschresearch/sofc-exp_textmining_resources/).
You can also use the [Hugginface Datasets implementation](https://huggingface.co/datasets/sofc_materials_articles).

<!-- Domains and Genres -->
* Materials Science
* Scientific Text


<!-- Any further references, links etc. -->
# References

    Annemarie Friedrich, Heike Adel, Federico Tomazic, Johannes Hingerl, Renou Benteau, Anika Maruscyk and Lukas Lange. [The SOFC-Exp Corpus and Neural Approaches to Information Extraction in the Materials Science Domain.](https://aclanthology.org/2020.acl-main.116/) ACL 2020.

