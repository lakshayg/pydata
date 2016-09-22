  ____        ____        _        
 |  _ \ _   _|  _ \  __ _| |_ __ _ 
 | |_) | | | | | | |/ _` | __/ _` |
 |  __/| |_| | |_| | (_| | || (_| |
 |_|    \__, |____/ \__,_|\__\__,_|
        |___/                      


This package provides several datasets to quickly get started
with machine learning or other data analysis tasks without
worrying about obtaining / formatting data. Currently, the
following datasets are available:

* Banana: http://mldata.org/repository/data/viewslug/banana-ida/
* CIFAR10: https://www.cs.toronto.edu/~kriz/cifar.html
* MAGIC04: https://archive.ics.uci.edu/ml/datasets/MAGIC+Gamma+Telescope
* Letter Recognition: https://archive.ics.uci.edu/ml/datasets/Letter+Recognition
* USPS Digits: http://www-i6.informatik.rwth-aachen.de/~keysers/usps.html
* Forest Cover Type: https://archive.ics.uci.edu/ml/datasets/Covertype
* MNIST: http://yann.lecun.com/exdb/mnist/

Installation
------------

To install the package, first clone the git repository using

$ git clone https://github.com/lakshayg/pydata

Now obtain the required datasets from the following link:

https://www.dropbox.com/sh/kicd5kwdv8n7kyi/AABqhGBnWHuu3n9EgjLfyOnQa?dl=1

Place the downloaded folder so that the directory structure looks
as follows:

pydata
|__ MANIFEST.in
|__ README.txt
|__ setup.py
|__ pydata
    |__ data          <<== this folder contains datasets
    :   |__ cifar10
    :   :   |__ ...
    :   |__ usps
    :   :   |__ ...
    :   |__ banana_data.csv
    :   |__ ...
    |__ datasets.py
    |__ __init__.py


The package is then installed using

$ python setup.py install

Usage
-----

Here is a short example demonstrating the use of pydata

>>> import pydata
>>> features, labels, metadata = pydata.load_banana()

