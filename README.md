# [Re] Three-dimensional wake topology and propulsive performance of low-aspect-ratio pitching-rolling plates

This repository contains the source files of the manuscript submitted to [ReScience C](https://rescience.github.io/).
The repository was forked from the [ReScience C template](https://github.com/ReScience/template).

Authors:

* Olivier Mesnard (The George Washington University)
* Lorena A. Barba (The George Washington University)

Abstract:

This article reports on a full replication study in computational fluid dynamics, using an immersed boundary method to obtain the flow around a pitching and rolling elliptical wing. As in the original study, the computational experiments investigate the wake topology and aerodynamic forces, looking at the effect of: Reynolds number (100--400), Strouhal number (0.4--1.2), aspect ratio, and rolling/pitching phase difference. We also include a grid-independence study (from 5 to 72 million grid cells). The trends in aerodynamic performance and the characteristics of the wake topology were replicated, despite some differences in results. We declare the replication successful, and make fully available all the digital artifacts and workflow definitions, including software build recipes and container images, as well as secondary data and post-processing code. Run times for each computational experiment were between 8.1 and 13.8 hours to complete 5 flapping cycles, using two compute nodes with dual 20-core 3.7GHz Intel Xeon Gold 6148 CPUs and two NVIDIA V100 GPU devices each.

## Compiling the article

Fill in information in [metadata.yaml](./metadata.yaml), modify [content.tex](content.tex), and type `make` command line.
This will produce an `article.pdf` using `xelatex` and provided font.
Note that you must have `make`, Python 3, and [PyYAML](https://pyyaml.org/) installed on your computer to compile the article.

After acceptance, we'll need to complete [metadata.yaml](./metadata.yaml) with information provided by the editor.
