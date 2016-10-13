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

Run the following command to download and install the package.
The script downloads datasets (~196MB) and installs python package

$ bash <(curl -s https://raw.githubusercontent.com/lakshayg/pydata/master/easy_setup.sh)

Usage
-----

API documentation is available at: https://lakshayg.github.io/pydata

Here is a short example demonstrating the use of pydata

>>> import pydata
>>> features, labels, metadata = pydata.load_banana()

