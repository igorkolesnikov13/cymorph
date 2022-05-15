---
title: 'CyMorph: fast non-parametric galaxy morphology package'
date: 03 May 2022
tags:
  - astronomy
  - morphology
  - python
  - cython
authors:
 - name: Igor Kolesnikov
   orcid: 0000-0002-1189-0112
   affiliation: "1"
 - name: Vitor Medeiros Sampaio
   orcid: 0000-0000-0000-0000
   affiliation: "2"
 - name: Reinaldo Ramos de Carvalho
   orcid: 0000-0000-0000-0000
   affiliation: "2"
affiliations:
 - name: Instituto Nacional de Pesquisas Espaciais, São José dos Campos, Brazil
   index: 1
 - name: NAT-Universidade Cruzeiro do Sul / Universidade Cidade de São Paulo, Rua Galvão Bueno, 868, 01506-000, São Paulo, SP, Brazil
   index: 2
bibliography: paper.bib
---


# Summary

We present CyMorph (Cython Morphology), a package that extracts specific metrics from a supplied 2d image. This revised and updated version is based on a code used in @teseRubens and @barchi2020machine. Metric extractions is done in a non-parametric way, namely there are no underlying assumptions about the 2d image distribution. The package relies heavily on the Cython language, which makes it much faster than the plain Python version, therefore suitable for large dataset analysis.

CyMorph is a fast and optimized package designed primarily to estimate five parameters characterizing the galaxy's morphology: 1) Concentration ($C$); 2) Asymmetry ($A$); 3) Smoothness ($S$); 4) Entropy ($H$); and the second moment of Gradient Pattern Analysis ($G_2$). The input image is expected to contain a single galaxy at the center and cleaned from contaminants (stars, other galaxies, etc). CyMorph has been used also to quantify the morphology of the temperature maps of the Intra-cluster medium (ICM) of clusters of galaxies. Finally, by design, metrics are source agnostic and will evaluate any 2d array supplied to the program.

CyMorph requires only an input image and, if needed, tuning of the parameters involved in the metrics definition. Preprocessing, such as cleaning and creation of the segmented image is required, but not included in CyMorph code.

# Statement of need

## Morphometry and physical proprieties of galaxies

When CyMorph is used to quantify galactic morphology, each metric is supposed to represent how a given physical mechanism alters the shape of the system and we know that this is true in several cases @conselice2003relationship. CyMorph estimates the following parameters:

- Concentration (C) -  measures how tight is the flux distribution of a given galaxy;
- Asymmetry (A) - as name says, it quantifies how symmetric the galaxy is;
- Smoothness (S) (also called Clumpiness) determines how clumpy the distribution is, being sensitive to the the presence of star-forming regions in a late-type galaxy; 
- Entropy (H) -  in this case we measure the Shannon entropy which reflects the average amount of information in the image, and
- $G_2$ - is the second moment of the image gradient pattern which gives the integral of all the assymetric vectors.

One of the most traditional systems designed to systematize the observed varieties of morphologies is based on Concentration, Asymmetry, and Smoothness e.g., @conselice2003relationship. These parameters have been used to study the physical properties of galaxies. Concentration is critical to distinguish between early- and late-type systems @conselice2003relationship. Also, as shown by @graham2001correlation, C well correlates with central velocity dispersion, galaxy size, luminosity, and black hole mass. [@conselice2000asymmetry; @conselice2003relationship] indicate that A is a good morphological indicator of galaxy interactions and mergers. These processes vary with redshift, so A may be valuable in extending the morphological analysis to the high redshift range. @conselice2003relationship studies how the S parameter may be associated to the star formation history. Early-type galaxies  (ETG) exhibit little signs of star formation and should result in low values of smoothness, while late-type galaxies (LTG) should have more pronounced star-forming regions, and by consequence, higher smoothness values, and in fact that is what is observed. The CAS system, together with H and $G_2$, is very effective  in distinguishing between early- and late-type galaxies and a combination of them may provide a solid intuition to find other classes still unknown. More important than having indicators that distinguish early- and late-type galaxies is that they reflect physical properties that can be examined in different environments and at different redshifts, probing the way galaxies evolve.

## Morphometry and Machine learning

Besides using morphometric parameters to study the actual physical processes molding galaxies directly, these parameters can also be used in Machine Learning (ML) methods to discriminate ETGs from LTGs. 
@barchi2020machine conduct a thorough study of ML using the CASHG2 metrics extracted with previous version of CyMorph as the primary input information to provide the classification between multiple combinations of morphological classes. Several ML algorithms were tested: Decision Tree (DT), Support Vector Machine (SVM), and Multilayer Perceptron (MLP). DT had a slightly better performance than the other two, with an overall accuracy (OA) of 98.5\%, when dealing only with bright galaxies. When applying Deep Learning (DL) technique, they find only a tiny increase in OA, 99.5\%. However, when classifying fainter galaxies, DL outperforms ML with 98.7\% against 94.8\%.

## Intra-cluster medium
CyMorph has been be used to study the temperature maps of the Intra-cluster medium (ICM) of rich clusters of galaxies. This use has proved valuable in understanding how cool-core and non cool-core clusters relate to the overall evolution of the system.  

# Acknowledgements

We thank CAPES and FAPESP for the financial support throughout this research.

# References