CyMorph
=======

*Non-parametric galaxy morphology python package*

*Updated, revised, and repacked version of 1st CyMorph version: https://github.com/rsautter/CyMorph & Paulo Barchi work*

About
-----

In the study of the way galaxies evolve, morphology is a key piece of information.
What we identify in an astronomical image is the result of several physical mechanisms
. The challenge is to be able to define a morphometric system that captures
the essence of the processes that transform a galaxy in the course of its evolution.

We present Cython Morphology (CyMorph), a revised and improved version of a non-parametric package to extract a list of morphometrics from the supplied image. Each of these metrics (except G2) ranges from 0 (min) to 1 (max) depending on the particular features of the content of the image.

There are several ways to use the metrics, ranging from studying galaxy
evolution in the context of Star-Formation Rate (SFR) `Sa Freitas (2022) <https://academic.oup.com/mnras/article-abstract/509/3/3889/6424948>`_ to  using the combination of the metrics as input for the machine learning network for classification as shown in 
`Barchi (2020) <https://www.sciencedirect.com/science/article/abs/pii/S2213133719300757>`_


To use CyMorph, it is only necessary to supply an image and, if needed, tune the parameters. The image preprocessing could be required to remove secondary sources, but it is not included in CyMorph code and is the end user's responsibility. It is dictated by the fact that each survey is different in optics, resolution, and storage routines (sky subtraction, object identification, or even cleaning). Each survey requires a specific and highly detailed image preparing algorithm (cleaning and segmentation).

CyMorph is organized as a list of classes, each class corresponding to a given metric. Core, computationally heavy functions are implemented in Cython and are called with the Python wrappers. Cython provides substantial speedup in comparison to pure Python code.

**Available metrics:**

- Concentration
- Asymmetry
- Smoothness
- Entropy
- Gradient Pattern Analysis (second moment)


Installation
------------

Dependencies ::

    pip install numpy scipy matplotlib seaborn sep

CyMorph ::

    pip install cymorph

Usage Guide
-----------

.. toctree::
   :maxdepth: 1

   tutorial
   metrics

.. toctree::
   :hidden:

   reference

For complete API documentation, see :doc:`reference`.

License
-------
The license for CyMorph is the MIT License.