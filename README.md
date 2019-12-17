## Semantic Set Similar Search Using Binarized LSH
By [Lele Chen](http://www.cs.rochester.edu/u/lchen63/) ,
Haitian Zheng,
[ Fatemeh Nargesian](http://www.cs.toronto.edu/~fnargesian/),
University of Rochester.


### Table of Contents
0. [Introduction](#introduction)
0. [Running](#running)


### Introduction

This repository is a course project in csc577.

### Running
0. This code is tested under Python 3.6 on Linux system.
0. Pytorch environment:[Pytorch 1.3](https://pytorch.org/). (conda install pytorch torchvision cudatoolkit=10.1 -c pytorch)
0. Install lshash:`cd lshash && python setup.py install`
0. Install torchtext:`pip install torchtext`
0. Install torchtext:`pip install wordfreq`
0. unzip the metadata under metadata forder

0. Run the demo code:
  - preprocess all data: `python data_preproce.py`
	- generate glove feature vector for each table: `python word2vec.py`
  - generate binary feature vector for each table: `python word2bit.py`
  - run binary LSH: `cd lshash` and then run `python test -q query_word -m binary`. For example: `python test -q professor -m binary` or `python test -q professor -m naive`



License
----

MIT
