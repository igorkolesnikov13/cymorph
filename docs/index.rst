CyMorph
=======

*Non-parametric galaxy morphology python package*

*Updated and adjusted and repacked version of 1st CyMorph version: https://github.com/rsautter/CyMorph & Paulo Barchi work*

About
-----
We present Cython Morphology (CyMorph), a revised and improved version of a non-parametric package to extract a list of metrics . CyMorph features the capability of extraction of the list of metrics from the supplied image. Each of these metrics (except G2) ranges from 0 (min) to 1 (max) depending on the particular features of the content of the image. We need to point that CyMorph does not classify the galaxies, but the combination of the metrics can be used as input for the machine learning network for classification as shown in 
`Barchi (2020) <https://www.sciencedirect.com/science/article/abs/pii/S2213133719300757>`_


To use CyMorph, it is only necessary to supply an image and, if needed, tune the parameters. The image preprocessing could be necessary, but it is not included in CyMorph code and is the end-user's responsibility. It is dictated by the fact that each survey is different in optics, resolution, and storage routines (sky subtraction, object identification, or even cleaning).  
Each survey requires a specific and highly detailed image preparing algorithm (cleaning and segmentation).

It is implemented ... in C with Python bindings via Cython

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

CyMorph (currently in tesing mode) ::

    pip install -i https://test.pypi.org/simple/ cymorph

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