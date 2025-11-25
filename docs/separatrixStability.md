# Proton Tunneling Pertubartion | Prism

![Cosmic Web example Image](https://topology-tool-kit.github.io/img/gallery/cosmicWeb.jpg)

## Pipeline description

This example computes the so-called *Bond Occurence Rate* from an ensemble of data-sets of electron density fields modeling a molecular system under a chemical perturbation. In this example, we visualize a phenomenon called *Proton Tunneling* on the *Prism Hexamer*. The datasets chosen in this example are extracted from (https://github.com/thom-dani/BondMatcher).

First, 

Second, the resulting density is slightly smoothed with the filter [ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html) (only `1` iteration).

Third, the density is normalized (in between 0 and 1) with the filter [ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html) to facilitate the subsequent processing steps.

Next, the data undergoes a first step of simplification with the filter [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html), to remove the least significant extrema (involved in a persistence pair with a persistence smaller than `0.3`).

Then, the [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html) is computed and saddle-saddle pairs with a persistence smaller than `0.3` are also simplified. 

Finally the geometry of the 1-separatrices and the 2-separatrices are slightly smoothed with the filter [GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html) (`10` iterations each). The resulting 1-separatrices are shown before simplification in the top-right inset and after simplification in the bottom-left inset. The bottom-right inset shows the 2-separatrices.

By adjusting the persistence simplification threshold, for the extrema in the filter [TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html), for the saddle-saddle pairs in the filter [MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html), the user can explore the patterns of the cosmic web at multiple scales of topological importance.

## ParaView

To reproduce the above screenshot, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
paraview states/cosmicWeb.pvsm
```

## Python code

``` python  linenums="1"
--8<-- "python/cosmicWeb.py"
```

To run the above Python script, go to your [ttk-data](https://github.com/topology-tool-kit/ttk-data) directory and enter the following command:
``` bash
pvpython python/cosmicWeb.py
```


## Inputs

- [ds14_scivis_0128_e4_dt04_1.0000.vtp](https://github.com/topology-tool-kit/ttk-data/raw/dev/ds14_scivis_0128_e4_dt04_1.0000.vtp): input particle data with a scalar array (function of dark matter density).

## Outputs

- `cosmicWeb.vtu`: skeleton of the cosmic web (1D separatrices connecting 2-saddles to maxima).

## C++/Python API

[GeometrySmoother](https://topology-tool-kit.github.io/doc/html/classttkGeometrySmoother.html)

[IcospheresFromPoints](https://topology-tool-kit.github.io/doc/html/classttkIcospheresFromPoints.html)

[MorseSmaleComplex](https://topology-tool-kit.github.io/doc/html/classttkMorseSmaleComplex.html)

[ScalarFieldNormalizer](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldNormalizer.html)

[ScalarFieldSmoother](https://topology-tool-kit.github.io/doc/html/classttkScalarFieldSmoother.html)

[TopologicalSimplificationByPersistence](https://topology-tool-kit.github.io/doc/html/classttkTopologicalSimplificationByPersistence.html)
