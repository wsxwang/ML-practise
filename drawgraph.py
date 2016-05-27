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
    print "minkowski, p = %s, sampling = %d"%(str(p), sampling);

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


if __name__ == "__main__":
    drawminkowski(10000, [1/float(10),1/float(2),1,2,3,10]);





