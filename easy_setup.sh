#!/bin/bash

git clone https://github.com/lakshayg/pydata
wget https://www.dropbox.com/sh/r5gn4z6m5871qnu/AAA_YwqQQbxdG5S4U6MG_SwTa?dl=1 -O data.zip
unzip data.zip -d pydata/pydata/data
cd pydata
sudo python setup.py install

