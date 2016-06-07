#-*-coding:utf-8-*-

"""
drawgraph.py
Wang Xiaoqi
create:2016-05-18

draw gragh of machine learning graphics
绘制机器学习相关图形
"""

import sys;
import os;
import math;
import numpy as np;
import matplotlib.pyplot as plt;
import random;

import kmeans
import fcm

"""
draw graphics two points which minkowski distance is 1
dimension is 2
point P is (0,0), point Q is (x,y)
minkowski distance n is 1, p will be given

画minkowski距离为1的两个点的图形
维度取2（公式中n取2）
公式参数p为输入
两个点P(0,0),Q(X,Y)

p:a list, default is [2](euclidean distance)
sampling:default is 10
"""
def drawminkowski(sampling =10, p = [2]):
    print "minkowski, p=%s, sampling=%d"%(str(p), sampling);

    X = np.linspace(-1, 1, sampling);

    plt.figure(figsize=(8,8), dpi=80);
    plt.xlabel("X");
    plt.ylabel("Y");
    plt.ylim(-1,1)
    plt.title("minkowski distance, distance = 1, p = " + str(p));

    plt.plot(np.linspace(-1, 1, 100), np.zeros(100), "k,", linewidth = 2);
    plt.plot(np.zeros(100), np.linspace(-1, 1, 100), "k,", linewidth = 2);

    for pi in p:
        if pi <= 0:
            continue;
        print pi;
        Y = np.power(1- np.power(np.abs(X), pi), 1/float(pi));
        print X;
        print Y;
        color = random.randint(1, 0xffffff);
        plt.plot(X,Y, label ="p=" + str(pi), color = "#" + format(color, "06x"), linewidth = 1);
        plt.plot(X,-Y, color = "#" + format(color, "06x"), linewidth = 1);

    plt.legend();
    plt.show();

"""
draw k-means gragh
data dimension is 2, which means flat gragh in 100*100

points:data set
centroids:cluster default centroids
p:minkowski distance parameter

绘制k-means算法图示
采用二维图示，即平面图(100*100)

points:数据集
k:各类别的初始质心
p:采用闵式距离作为距离公式，参数p值
"""
def drawkmeans(points, centroids, p):
    print "k-means:n=",len(points),", k=",len(centroids),", p=",p;
    assert(len(points) > 0);
    assert(len(centroids) > 0);
    assert(p > 0);
    
    plt.figure(figsize=(8,8), dpi=80);
    plt.xlabel("X");
    plt.ylabel("Y");
    plt.ylim(-100,100)
    plt.plot(np.linspace(-100, 100, 100), np.zeros(100), "k,", linewidth = 2);
    plt.plot(np.zeros(100), np.linspace(-100, 100, 100), "k,", linewidth = 2);

    clusters, turn=kmeans.alg_kmeans(points, centroids, p);
    print turn, "turns";
    print "clusters:", clusters;
    plt.title("k-means, %d points, k=%d, p=%d, turns=%d"%(len(points),len(centroids),p, turn));
    for c in clusters:
        if len(c) == 0:
            continue;
        X = [];
        Y = [];
        for idx in c:
            point = points[idx];
            X.append(point[0]);
            Y.append(point[1]);
        centroidOfc = [sum(X)/len(X), sum(Y)/len(Y)];
        # choose color and style
        color=random.randint(1, 0xffffff);
        color="#" + format(color, "06x");
        shape=".,ov^<>1234sphHd|_+x";
        shape=shape[random.randint(0, len(shape) - 1)];
        shape +=':';
        plt.plot(X,Y, shape, color=color, linewidth = 1);
        # annotate
        plt.annotate(str(len(c))+"points", xy=centroidOfc, xycoords='data',color='r');
        # centroids of clusters
        plt.plot(centroidOfc[0], centroidOfc[1], "*r");
        
    plt.legend();
    plt.show();

"""
draw fcm gragh
data dimension is 2, which means flat gragh in 100*100

points:data set
u:default u matrix, degree of membership of data point in cluster
m:
p:minkowski distance parameter
e:terminate number

绘制fcm算法图示
采用二维图示，即平面图(100*100)

points:数据集
u:初始归属概率矩阵
m:权值
p:采用闵式距离作为距离公式，参数p值
e:终止参数值
"""
def drawfcm2(points,u,m,p,e):
    assert(len(points) > 0);
    assert(len(u) == len(points));
    assert(len(u[0]) > 0);
    assert(m > 0);
    assert(p > 0);
    assert(e > 0);
    c=len(u[0]);
    print "fcm:n=",len(points),", c=",c,", m=",m,", p=",p,", e=",e;

    plt.figure(figsize=(8,8), dpi=80);
    plt.xlabel("X");
    plt.ylabel("Y");
    plt.ylim(-100,100)

    plt.plot(np.linspace(-100, 100, 100), np.zeros(100), "k,", linewidth = 2);
    plt.plot(np.zeros(100), np.linspace(-100, 100, 100), "k,", linewidth = 2);

    u2,turn=fcm.alg_fcm(points, u, m, p, e);
    plt.title("fcm, %d points, c=%d, m=%d, p=%d, e=%f, turns=%d"%(len(points),len(u[0]), m, p, e, turn));
    print turn,"turns";
    print "last u:", u2;
    clusters = [[] for i in range(c)];
    for i in range(len(u2)):
        maxu = max(u2[i]);
        ci = u2[i].index(maxu);
        clusters[ci].append(points[i]);
    print "clusters:",clusters;

    for c in clusters:
        if len(c) == 0:
            continue;
        c = [[r[col] for r in c] for col in range(2)];
        centroidOfc = [sum(c[0])/len(c[0]), sum(c[1])/len(c[1])];
        # choose color and style
        color=random.randint(1, 0xffffff);
        color="#" + format(color, "06x");
        shape=".,ov^<>1234sphHd|_+x";
        shape=shape[random.randint(0, len(shape) - 1)];
        shape +=':';
        plt.plot(c[0],c[1], shape, color=color, linewidth = 1);
        # annotate
        plt.annotate(str(len(c[0]))+"points", xy=centroidOfc, xycoords='data',color='r');
        # centroids of clusters
        plt.plot(centroidOfc[0], centroidOfc[1], "*r");
        
    plt.legend();
    plt.show();

def testkmeans(points):
    print "-----k-means-----";    
    k = random.randint(2,15);
    centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
    p = random.randint(1,3);
    print "default centroids:", centroids;
    drawkmeans(points, centroids, p);

def testfcm(points):
    print "-----fcm-----";   
    c = random.randint(2,5);
    m = random.randint(2, 10);
    p = random.randint(1,3);
    e = random.random();
    if e == 0:
        e = 0.5;
    u = [[0 for j in range(c)] for i in range(pointscount)]
    for i in range(pointscount):
        u[i][0] = random.random();
        u[i][1] = 1 - u[i][0];
    print "default u:", u;
    drawfcm2(points,u,m,p,e);
    
if __name__ == "__main__":
    drawminkowski(10000, [1/float(10),1/float(2),1,2,3,10]);

    # data points
    pointscount = random.randint(10,100);
    points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
    print pointscount, " points:\n", points;

    #fcm
    testfcm(points);

    #k-means
    testkmeans(points);







