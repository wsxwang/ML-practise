#-*-coding:utf-8-*-

"""
k-means.py
Wang Xiaoqi
create:2016-05-29

K-means algrithm
K-means 算法实现
"""

import sys;
import os;
import numpy as np;
import random;

from distance import *

"""
calculate minkowsky distance
P,Q:two vectors(list), same dimension

计算闵氏距离
P,Q是两个同维向量

K-means algrithm
use minkowski distance to calculate centroids of cluster
points:data set, each point is a vector with same dimention
k:k initial centroids of clusters
p:minkowski distance parameter
ret:k cluster of points

K-means算法
points:给定的同维向量数据集合
距离算法采用闵氏距离
kcentroids:k个分类的初始质心
p:闵氏距离的参数p值
返回值:k个数据集合
"""
def alg_kmeans(points, kcentroids, p):
    """
    print points;
    print kcentroids
    print p;
    """
    assert(len(points) > 1);
    assert(len(kcentroids) > 1);
    assert(len(points[0]) == len(kcentroids[0]));

    k = len(kcentroids);
    clusters = [[] for row in range(k)];
    centroids = kcentroids;
    nochange = False;

    print len(clusters);
    print clusters;
    
    while nochange == False:
        for point in points:
            # cal distance to each centroid
            mindis = sys.float_info.max;
            clusteridx = -1;
            for i in range(0, k):
                dis = dis_minkowski(point, centroids[i], p);
                if dis < mindis:
                    clusteridx = i;
                   # clusters[i].
                    
             #   dis[i] = ;
                
            # point -> cluster

        # recalculate centroids for each cluster
        """
        for point in clusters:
            print point;
        """  
        break;
    return clusters;


"""
------------------------------------------------------------------------
test function
dimention=2, p=2 euclidean distance, 10 points, cluster 4
基于欧式几何距离，即维度2，p值2，10个点，分为4类
"""
def test():
    points = [
        [10,10],[10,9],[8,9],
        [-5,-6],[-3,-2],
        [10, -3],[8,-5],
        [-7,2],[-9,9],[-9,8]
        ];
    kcentroids = [
        [random.randint(-1000, 1000), random.randint(-1000, 1000)],
        [random.randint(-1000, 1000), random.randint(-1000, 1000)],
        [random.randint(-1000, 1000), random.randint(-1000, 1000)],
        [random.randint(-1000, 1000), random.randint(-1000, 1000)],
        ];

    clusters = alg_kmeans(points, kcentroids, 2);

    assert(len(clusters) == 4);
    print clusters;
    
if __name__ == "__main__":
    test();

           
    

