#!/usr/bin/env bash

conda create -c conda-forge -n keras python==3.9.19
#conda activate keras
#exit
conda install -c conda-forge -n keras tensorflow-gpu tensorflow keras keras-core matplotlib pandas

pip install keras_cv==0.6.0 
#pip install tensorflow-gpu
#pip install -U tensorflow
#pip install keras-core
#pip install matplotlib
#pip install pandas
