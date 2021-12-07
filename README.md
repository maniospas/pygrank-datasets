# pygrank-datasets
This repository generates and hosts synthetic graph datasets with 
community structures. These can used by the 
[pygrank](https://github.com/MKLab-ITI/pygrank) package.

**License:** Apache Software License
<br>**Author:** Emmanouil (Manios) Krasanakis
<br>**Dependencies:** None

# :zap: Quickstart
Given that `pygrank` has been installed (e.g. with pip) it can automatically
parse datasets hosted in this repository. For example, the *graph9* 
dataset can be automatically downloaded and imported with the following code:
```python
>>> import pygrank as pg
>>> graph, groups = next(pg.load_one_community('graph9'))
```


# :thumbsup: Contributing
Contributions can be discussed in [pygrank's issue tracker](https://github.com/MKLab-ITI/pygrank/issues) or by participating in [discussions]().
To introduce new datasets, you need to create a top-level folder with the same,
name as the dataset and create a `[dataset]/edges.txt` 
file with pairs of graph nodes that form
edges (each pair must be placed in a new line with its nodes separated with
a tab or space) and a `[dataset]/groups.txt` file whose lines correspond
to sets of nodes belonging in communities (each community occupies a different line).

# :notebook: Citation
If you use some of these datasets in your research, please cite `pygrank`'s publication:
```
@misc{krasanakis2021pygrank,
      title={pygrank: A Python Package for Graph Node Ranking}, 
      author={Emmanouil Krasanakis, Symeon Papadopoulos, Ioannis Kompatsiaris, Andreas Symeonidis},
      year={2021},
      eprint={2110.09274},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}
```
