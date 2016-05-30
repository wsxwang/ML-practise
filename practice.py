#-*-coding:utf-8-*-

"""
practice.py
Wang Xiaoqi
create:2016-05-29

机器学习的练习程序

"""

import sys;
import os;
import numpy as np;
import matplotlib.pyplot as plt;
import random;

from k_means import *

"""
------------------------------------------------------------------------
test function
"""

"""
k-means test function
"""
def test_kmeans():
    assert(alg_kmeans() == 0);
    
if __name__ == "__main__":
    test_kmeans();

           
    

