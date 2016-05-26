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
#import numpy as np;
#import matplotlib.pyplot as plt;

"""
draw graphics two points which minkowsky distance is 1
dimension is 2
point P is (0,0), point Q is (x,y)
minkowsky distance n is 1, p will be given

画minkowsky距离为1的两个点的图形
维度取2（公式中n取2）
公式参数p为输入
两个点P(0,0),Q(X,Y)

p:default is 2(euclidean distance)
sampling:default is 10, means x={-1,-0.9,...,0.9,1}
"""
def drawminkowsky(sampling =10, p = 2):
    print "minkowsky, p = %d, sampling = %d"%(p, sampling);
    X = range(sampling * -1, 0) + range(0, sampling +1);
    for x in X:
        xf = x/float(sampling);
        Y = minkowsky_QY(xf, p);
        for y in Y:
            print (xf, y);

"""
known minkowsky distance, point P, p, x of point Q, get y of point Q
dimension is 2

在2维前提下
已知闵氏距离、点P、计算参数p以及点Q的x坐标，求点Q的y坐标

P=(0,0), distance d=1
"""
def minkowsky_QY(x, p):
    y = 1 - math.pow(math.fabs(x),p);
    return [-y,y];

if __name__ == "__main__":
    drawminkowsky(100, 3);





