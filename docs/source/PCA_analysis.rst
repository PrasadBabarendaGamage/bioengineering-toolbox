PCA analysis
============
   
.. toctree::
   :maxdepth: 2
  

Introduction
------------
PCA is a simple, non-parametric method of extracting relevant information from confusing data sets. It provides a roadmap for how to reduce a complex data set to a lower dimension to reveal its sometimes hidden underlying dynamics :cite:`Shlens2003`.

Motivation: a toy example
-------------------------
We often do not know what measurements best reflect the dynamics of our system in question. Noise contaminates our data set only serving to obfuscate the dynamics further. 

The Goal: Principal component analysis computes the most meaningful basis to re-express a noisy, garbled data set. The hope is that this new basis will filter out the noise and reveal hidden dynamics.

For each time sample (experimental trial, or model), we have a set of data describing the positions of the skin boundary of the breast mesh (equivalent to having multiple measurements (e.g. voltage, position, etc.). The number of measurement types is the dimension of the data set.


In general, each data sample is a vector in m-dimensional space (e.g. 3-D, x, y z positions), where m is the number of measurement types (e.g. 3). 
Equivalently, every time sample is a vector that lies in an m-dimensional vector space spanned by an orthonormal basis. All measurement vectors in this space are a linear combination of this set of unit length basis vectors.






.. bibliography:: refs.bib
   :style: plain
