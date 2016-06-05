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
points:data set, each point is a vector with same dimension
kcentroids:k initial centroids of clusters
p:minkowski distance parameter
ret:k cluster of points index

K-means算法
points:给定的同维向量数据集合
距离算法采用闵氏距离
kcentroids:k个分类的初始质心
p:闵氏距离的参数p值
返回值:k个数据集合，元素是points的下标
"""
def alg_kmeans(points, kcentroids, p):
    assert(len(points) > 1);
    assert(len(kcentroids) > 1);
    assert(len(points[0]) == len(kcentroids[0]));

    k = len(kcentroids);
    # centroids for clusters, each centroid is a vector
    centroids = kcentroids;
    # clusters, set of point's index
    c1 = [[] for row in range(k)];
    c2 = [[] for row in range(k)];

    change = True;
    while change:
        change = False;
        # cluster once
        c2 = PointstoCluster(points, centroids, p);
        # if cluster change
        change = (cmp(c1,c2) != 0);
        # if not change, do again
        if change:
            c1 = c2;
            # recalculate cluster centroids
            centroids = RecalculateCentroids(points, k, c2);
    return c2;

"""
cluster points to K clusters according to the distance to each centroid
根据到质心的距离，将数据分为K个类

use minkowski distance to calculate centroids of cluster
points:data set, each point is a vector with same dimension
kcentroids:centroids of clusters
p:minkowski distance parameter
ret:k cluster of points index

points:给定的同维向量数据集合
距离算法采用闵氏距离
kcentroids:k个分类的质心
p:闵氏距离的参数p值
返回值:k个数据集合，元素是points的下标
"""
def PointstoCluster(points, kcentroids, p):
    assert(len(points) > 1);
    assert(len(kcentroids) > 1);
    assert(len(points[0]) == len(kcentroids[0]));

    k = len(kcentroids);
    clusters = [[] for i in range(k)];
    
    for i in range(len(points)):
        # cal distance to each centroid
        mindis = sys.float_info.max;
        point = points[i];
        clusteridx = -1;
        for j in range(0, k):
            dis = dis_minkowski(point, kcentroids[j], p);
            if dis < mindis:
                clusteridx = j;
                mindis = dis;
        clusters[clusteridx].append(i);

    return clusters;

"""
recalculate centroid of cluster
重新计算每个类别的质心

points:data set, each point is a vector with same dimension
k:number of clusters
clusters:cluster item is a list of points' index
ret:k cluster centroids

points:给定的同维向量数据集合
k:分类数目
clusters:分类的列表，每个元素是一个list，list元素是point是的下标
返回值:新的k个分类的质心list
"""
def RecalculateCentroids(points, k, clusters):
    assert(len(points) > 1);
    assert(k > 1);

    dimension = len(points[0]);
    centroids = [[0 for d in range(dimension)] for row in range(k)];
    for i in range(k):
        if len(clusters[i]) == 0:
            continue;
        for d in range(0, dimension):
            centroids[i][d] = 0;
            for pidx in clusters[i]:
                centroids[i][d] += points[pidx][d];
            centroids[i][d] /= len(clusters[i]);
    return centroids;

"""
------------------------------------------------------------------------
test function
dimension=2, p=2 euclidean distance, 10 points, cluster 4
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
        [random.randint(-10, 10), random.randint(-10, 10)],
        [random.randint(-10, 10), random.randint(-10, 10)],
        [random.randint(-10, 10), random.randint(-10, 10)],
        [random.randint(-10, 10), random.randint(-10, 10)],
        ];

    clusters = alg_kmeans(points, kcentroids, 2);

    assert(len(clusters) == 4);
    print clusters;
    
if __name__ == "__main__":
    test();

           
    

