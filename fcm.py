#-*-coding:utf-8-*-

"""
fcm.py
Wang Xiaoqi
create:2016-06-06

fcm algrithm
fcm 算法实现
"""

import sys;
import os;
import numpy as np;
import random;

from distance import *

"""
fcm algrithm
points:data set, each point is a vector with same dimension(n points)
u:matrix of the degree of the membership of data point in some cluster(n*c)
m:any real number
p:minowski distance parameter, use minkowski distance to meassure proxity of data point and cluster
e:N+
terminateturn:terminate iteration turn, 0 based
ret:(terminated u matrix, calculate turns (0 based))

fcm算法
points:给定的同维向量数据集合（数目为n）
u:points中数据点归属到各个分类的当前归属概率矩阵（n*c）
m:权重
p:距离算法采用闵氏距离的参数p值
e:终止值（实数）
terminateturn:终止迭代的轮次，从0开始
返回值:一个tuple:(最终计算过后的u矩阵,计算轮次（从0开始）)
"""
def alg_fcm(points,u,m,p,e, terminateturn=sys.maxint):
    assert(len(points) == len(u));
    assert(len(points) > 0);
    assert(len(u[0]) > 0);
    assert(m > 0);
    assert(p > 0);
    assert(e > 0);

    u1 = u;
    k = 0;
    while(True):
        # calculate one more turn
        u2 = fcm_oneturn(points, u1, m, p);
        # max difference between u1 and u2
        maxu = fcm_maxu(u1,u2);
        
        if (maxu < e):
            break;
        u1 = u2;
        k=k+1;
        if k > terminateturn:
            break;
        
    return (u2, k);

"""
do on turn of fcm
parameters and ret:sam as alg_fcm

fcm算法计算一轮
参数和返回值同alg_fcm
"""
def fcm_oneturn(points, u, m, p):
    assert(len(points) == len(u));
    assert(len(points) > 0);
    assert(len(u[0]) > 0);
    assert(m > 0);
    assert(p > 0);

    n = len(points);
    c = len(u[0]);

    # calculate centroids of clusters
    centroids = fcm_c(points, u, m);
    assert(len(centroids) == c);
    
    # calculate new u matrix
    u2 = fcm_u(points, centroids, m, p);
    assert(len(u2) == n);
    assert(len(u2[0]) == c);
    
    return u2;

"""
get max difference between matrix u1 and u2 item
两轮计算得到的归属概率矩阵，求其元素最大差距
"""
def fcm_maxu(u1,u2):
    assert(len(u1) == len(u2));
    assert(len(u1) > 0);
    assert(len(u1[0]) > 0);

    ret = 0;
    n = len(u1);
    c = len(u1[0]);
    for i in range(n):
        for j in range(c):
            ret = max(np.fabs(u1[i][j] - u2[i][j]), ret);
    
    return ret;

"""
calclulate centroids of clusters
points:同alg_fcm
u:u matrix
m:同alg_fcm
ret:[c1,c2,...,cc]

计算各个分类的质心
points:同alg_fcm
u:归属概率矩阵
m:同alg_fcm
返回值：质心行向量[c1,c2,...cc]
"""
def fcm_c(points, u, m):
    assert(len(points) == len(u));
    assert(len(points) > 0);
    assert(len(u[0]) > 0);
    assert(m > 0);

    n = len(points);
    c = len(u[0]);
    ret = [];
    for j in range(c):
        sum1 = 0;
        sum2 = 0;
        for i in range(n):
            sum2 += np.power(u[i][j], m);
            sum1 += np.dot(points[i], np.power(u[i][j], m));
        cj = sum1 /sum2;
        ret.append(cj);

    return ret;

"""
recalculate u matrix
points:same as alg_fcm
centroids:return of fcm_c
m:same as alg_fcm
p:same as alg_fcm
ret:new u matrix

重新计算归属概率矩阵
points:同alg_fcm
centroids:质心向量，fcm_c的返回值
m:同alg_fcm
p:同alg_fcm
返回值:新的归属概率矩阵
"""
def fcm_u(points, centroids, m, p):
    assert(len(points) > 0);
    assert(len(centroids) > 0);
    assert(m > 0);
    assert(p > 0);

    n = len(points);
    c = len(centroids);
    ret = [[0 for j in range(c)] for i in range(n)];
    for i in range(n):
        for j in range(c):
            sum1 = 0;
            d1 = dis_minkowski(points[i],centroids[j],p);
            for k in range(c):
                d2 = dis_minkowski(points[i],centroids[k],p);
                sum1 += np.power(d1/d2, float(2)/(float(m)-1));
            ret[i][j] = 1/sum1;

    return ret;


"""
------------------------------------------------------------------------
test function
dimension=2, p=2 euclidean distance, 10 points, cluster 2
基于欧式几何距离，即维度2，p值2，10个点，分为2类
"""
def test():
    points = [
        [10,10],[10,9],[8,9],
        [-5,-6],[-3,-2],
        [10, -3],[8,-5],
        [-7,2],[-9,9],[-9,8]
        ];
    u = [[random.random(), 0] for i in range(10)]
    for i in u:
        i[1] = 1-i[0];
    m=2;
    p=2;
    e=0.1;

    u2, turn=alg_fcm(points, u, m, p, e);

    assert(len(u2) == 10);
    assert(len(u2[0]) == 2);
    print turn," turns\n",u,"\n",u2;
    
if __name__ == "__main__":
    test();

           
    

