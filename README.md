# CyMorph - non-parametric galaxy morphology package
_Updated and adjusted and repacked version of 1st CyMorph version:
https://github.com/rsautter/CyMorph & Paulo Barchi work_

## About

We present Cython Morphology (CyMorph), a revised and improved version of a non-parametric package to extract a list of morphometrics from the supplied image. Each of these metrics (except G2) ranges from 0 (min) to 1 (max) depending on the particular features of the content of the image. In the study of the way galaxies evolve, morphology is a key piece of information.
What we identify in an astronomical image is the result of several physical mechanisms.

To use CyMorph, it is only necessary to supply an image and, if needed, tune the parameters. The image preprocessing could be required to remove secondary sources, but it is not included in CyMorph code and is the end user's responsibility. It is dictated by the fact that each survey is different in optics, resolution, and storage routines (sky subtraction, object identification, or even cleaning). Each survey requires a specific and highly detailed image preparing algorithm (cleaning and segmentation).

CyMorph is organized as a list of classes, each class corresponding to a given metric. Core, computationally heavy functions are implemented in Cython and are called with the Python wrappers. Cython provides substantial speedup in comparison to pure Python code.

### Available metrics:

- Concentration
- Asymmetry
- Smoothness
- Entropy
- Gradient Pattern Analysis (second moment)

## Installation
Dependencies:
```
pip install numpy scipy matplotlib seaborn sep
```
CyMorph can be installed with:
```
pip install cymorph
```

## Documentation
https://cymorph.readthedocs.io/

## Basic Usage


### Concentration
```
from cymorph.concentration import Concentration
c = Concentration(image, radius1, radius2) 
c.get_concentration()
```

### Asymmetry
```
from cymorph.asymmetry import Asymmetry
a = Asymmetry(image) 
a.get_pearsonr()
a.get_spearmanr()
a.get_collected_points_plot()
```

### Smoothness
```
from cymorph.smoothness import Smoothness
s = Smoothness(clean_image, segmented_mask, smoothing_degradation, butterworth_order) 
s.get_pearsonr() 
s.get_spearmanr()
s.get_smoothed_image()
s.get_collected_points_plot()
```


### Entropy
```
from cymorph.entropy import Entropy
e = Entropy(image, bins) 
e.get_entropy()
```


### G2
```
from cymorph.g2 import G2
g2 = G2(g2_modular_tolerance, g2_phase_tolerance, g2_position_tolerance) 
g2.get_g2()
g2.get_gradient_plot()
g2.get_asymmetry_gradient_plot()
```

### Contributors

- Igor Kolesnikov
- Vitor Sampaio
- Paulo Barchi
- Rubens Sautter