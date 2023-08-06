# grapheno
A GPU-accelerated implementation of [PhenoGraph](https://github.com/jacoblevine/PhenoGraph) using [NVIDIA RAPIDS](https://github.com/rapidsai) for fast single-cell phenotyping.

## Installation
Install RAPIDS into new environment:
```
$ conda create -n rapids-21.12 -c rapidsai-nightly -c nvidia -c conda-forge rapids=21.12 python=3.8 cudatoolkit=11.2
```

Install grapheno:
```
$ pip install grapheno
```

(Optional) Install holoviews for visualization:
```
$ conda install -c pyviz holoviews bokeh
```

## Usage
```
import cudf
import cuml
import grapheno

X, _ = cuml.make_blobs(n_samples=100000,n_features=20,centers=5)
X = cudf.DataFrame.from_records(X)
communities, G, Q = grapheno.cluster(X)
```

## Benchmarking
See benchmark.ipynb for comparisons between grapheno (GPU) and phenograph (CPU) and to regenerate the figures below.

GPU is orders of magnitude faster than CPU at large data scales. Mean points and error bars are from three replicates:
![benchmarking times](img/benchmark.png)

Modularity is comparable between GPU and CPU implementations. t-SNE embeddings of simulated data colored by cluster label:
![benchmarking tsne](img/tsne.png)
