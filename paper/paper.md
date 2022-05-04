---
title: 'CyMorph: non-parametric galaxy morphology package'
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

We present Cython Morphology (CyMorph), a package that extracts metrics from the supplied 2d array. This revised and updated version is based on [@teseRubens; @barchi2020machine]. It does not require any additional information on the image's content, so it is called non-parametric. 
In the context of galaxy morphology, CyMorph is a fast and optimized package that provides five morphometrics already known to the scientific community: Concentration (C), Asymmetry (A), Smoothness (S), Entropy (H), and second moment of Gradient Pattern Analysis (G2). Usually, this set of metrics is used with galaxies. The input image will contain a single galaxy in the center in such a case. 
Apart from galaxy morphology, CyMorph was also used with gas clusters and short $\gamma$-ray bursts. Finally, by design, metrics are source agnostic and will evaluate any 2d array supplied to the program.
To use CyMorph, it is necessary to supply an image and, if needed, tune the
parameters of the metrics. The image preprocessing could be required,
but it is not included in CyMorph code and is the end user's responsibility.


# Statement of need

## Morphometry and physical proprieties of the galaxies

In the case of galactic morphology, each metric measures patterns and forms in the image:
Concentration measures how tightly pixels are distributed in the galaxy structure. 
Asymmetry measures the irregularity of the shape of the galaxy's disk and bulge. 
Smoothness evaluates the presence of the small structures in the galaxy's disk (star-forming regions). 
Entropy is the measure of the heterogeneity of the pixel distribution. 
G2 analyses the vector field of the flux distribution and counts the variation of flux intensity. 

One of the most traditional methods to systematize the observed varieties of morphologies is based on Concentration, Asymmetry, and Smoothness (e.g., @conselice2003relationship). These parameters have been used to study the physical properties of galaxies. Concentration is associated with the Bulge to Total light ratio, which can be an important discriminant between spirals and ellipticals @conselice2003relationship. Besides, @graham2001correlation has shown that C may correlate with velocity dispersion, galaxy size, luminosity, and black hole mass. [@conselice2000asymmetry; @conselice2003relationship] have shown that A is a good morphological indicator of galaxies undergoing galaxy interactions and mergers. These processes vary with redshift, so A may be valuable in extending the morphological analysis to the high redshift range. Also, @conselice2003relationship studied how the S indicator may reveal how clumpy galaxies are and how this reflects their star formation history. Ellipticals exhibit little signs of star formation and should show up as smooth light distributions, while spirals with active star formation should have a more pronounced smoothness. This is, in fact, what they observe. S can be effective in distinguishing ETGs from LTGs. When applied to an image with a clearly elliptical galaxy, usually, C will have high values, and A, S, H, and G2 will have low values. While in the case of a clearly spiral galaxy, it would be the opposite. Combining these values can provide a solid intuition of the class of unknown galaxies. More important than having indicators that separate ellipticals and spirals is that they reflect physical properties that can be examined in different environments and at different redshifts, probing the way galaxies evolve.

## Morphometry and Machine learning

Besides using the morphometric parameters to study the actual physical processes molding galaxies directly, they can also be used in Machine Learning (ML) methods to discriminate ETGs from LTGs. 
@barchi2020machine conducts a thorough study of ML using the CASHG2 system as the primary input information and Galaxy Zoo 1, [@lintott2008galaxy; @lintott2011galaxy] to provide the "true" classification. Several ML algorithms were tested: Decision Tree (DT), Support Vector Machine (SVM), and Multilayer Perceptron (MLP). DT had a slightly better performance than the other two, with an overall accuracy (OA) of 98.5\%, when dealing only with bright galaxies. When applying Deep Learning (DL) technique, they find only a tiny increase in OA, 99.5\%. However, when classifying fainter galaxies, DL outperforms ML with 98.7\% against 94.8\%.

## Intracluster medium
CyMorph can also be applied to X-Ray map tracing gas from the Intracluster medium (ICM). By combining the results of the galaxy's morphology and ICM hot gas X-Ray morphology properties, we plan to investigate how the cluster's ICM morphological properties (high asymmetry, for example) affect member galaxies' morphology. 

## Short $\gamma$-ray burst(GRB)
CyMorph was also used by Santana-Silva et al. (in prep.) to trace galaxy properties that are typical for $\gamma$-ray burst(GRB) hosts in order to prioritize targets with similar characteristics during gravitational wave optical follow-ups. 

# Acknowledgements

We want to thank _CAPES_ and _FAPESP_ for the financial support of this research.

# References