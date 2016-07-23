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
import Tkinter as tk;

import drawgraph as dr;

"""
弹出聚类算法面板
"""
def btfunc_cluster():
    frame=tk.Toplevel();
    createClusterWidgets(frame);
    frame.mainloop();

def btfunc_elementaryfunc():
    frame=tk.Toplevel();
    createElementaryfuncWidgets(frame);
    frame.mainloop();

"""
------------------------------------------------------------------------
cluster frame
聚类算法演示
"""
class ClusterInfo:
    points = None;
    centroids = None;
    u = None;
    c_terminateturn = None;
    c_n = None;
    c_p = None;
    c_k = None;
    c_c = None;
    c_e = None;
    
"""
绘制聚类算法面板
"""
def createClusterWidgets(master):
    master.title("cluster practie");

    tk.Label(master, text="terminate turn=").grid(row=0,column=0, sticky=tk.W);
    clusterinfo.c_terminateturn = tk.Entry(master, width=10);
    clusterinfo.c_terminateturn.insert(0, str(sys.maxint));
    clusterinfo.c_terminateturn.grid(row=0,column=1);
    tk.Button(master, text="k-means",width=10, command=btfunc_kmeans).grid(row=0,column=2);
    tk.Button(master, text="fcm2", width=10, command=btfunc_fcm2).grid(row=0,column=3);
    tk.Button(master, text="fcm1", width=10, command=btfunc_fcm1).grid(row=0,column=4);

    tk.Label(master, text="data point set config:").grid(row=1,column=0, sticky=tk.W,columnspan=2);
    tk.Label(master, text="n=").grid(row=2,column=0, sticky=tk.W);
    clusterinfo.c_n = tk.Entry(master, width=10);
    clusterinfo.c_n.insert(0, "100");
    clusterinfo.c_n.grid(row=2,column=1);
    tk.Label(master, text="data points:").grid(row=3,column=0, sticky=tk.W);
    tk.Button(master, text="random",width=10, command=btfunc_randompoints).grid(row=3,column=1);
    
    tk.Label(master, text="Minkowski distance config:").grid(row=1,column=3, sticky=tk.W,columnspan=2);
    tk.Label(master, text="p=").grid(row=2,column=3, sticky=tk.W);
    clusterinfo.c_p = tk.Entry(master, width=10);
    clusterinfo.c_p.insert(0, "2");
    clusterinfo.c_p.grid(row=2,column=4);
    
    tk.Label(master, text="K-means config:").grid(row=10,column=0, sticky=tk.W,columnspan=2);
    tk.Label(master, text="k=").grid(row=11,column=0, sticky=tk.W);
    clusterinfo.c_k = tk.Entry(master, width=10);
    clusterinfo.c_k.insert(0, "3");
    clusterinfo.c_k.grid(row=11,column=1);
    tk.Label(master, text="initial centroids:").grid(row=12,column=0, sticky=tk.W);
    tk.Button(master, text="random",width=10, command=btfunc_randomcentroids).grid(row=12,column=1);
    
    tk.Label(master, text="fcm config:").grid(row=10,column=3, sticky=tk.W,columnspan=32);
    tk.Label(master, text="m=").grid(row=11,column=3, sticky=tk.W);
    clusterinfo.c_m = tk.Entry(master, width=10);
    clusterinfo.c_m.insert(0, "2");
    clusterinfo.c_m.grid(row=11,column=4);
    tk.Label(master, text="c=").grid(row=12,column=3, sticky=tk.W);
    clusterinfo.c_c = tk.Entry(master, width=10);
    clusterinfo.c_c.insert(0, "3");
    clusterinfo.c_c.grid(row=12,column=4);
    tk.Label(master, text="ε=").grid(row=13,column=3, sticky=tk.W);
    clusterinfo.c_e = tk.Entry(master, width=10);
    clusterinfo.c_e.insert(0, "0.001");
    clusterinfo.c_e.grid(row=13,column=4);
    tk.Label(master, text="initial Uij:").grid(row=14,column=3, sticky=tk.W);
    tk.Button(master, text="random",width=10, command=btfunc_randomumatrix).grid(row=14,column=4);

    btfunc_randompoints();
    btfunc_randomcentroids();
    btfunc_randomumatrix();
        
def btfunc_randompoints():
    pointscount = int(clusterinfo.c_n.get());
    clusterinfo.points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
    print "random points:\n", clusterinfo.points;

def btfunc_randomcentroids():
    k = int(clusterinfo.c_k.get());
    clusterinfo.centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
    print "random centroids:\n", clusterinfo.centroids;

def btfunc_randomumatrix():
    c = int(clusterinfo.c_c.get());
    pointscount = int(clusterinfo.c_n.get());
    clusterinfo.u = [[0 for j in range(c)] for i in range(pointscount)];
    for i in range(pointscount):
        for j in range(c-1):
            leftrange = c*10-sum(clusterinfo.u[i])-1;
            if leftrange == 0:
                break;
            clusterinfo.u[i][j] = random.randint(0, leftrange);
        if sum(clusterinfo.u[i]) == 0:
            clusterinfo.u[i][0] = 1;
        clusterinfo.u[i][c-1] = c*10-sum(clusterinfo.u[i]);
    clusterinfo.u = np.dot(clusterinfo.u, 1/float(c*10));
    print "random Uij:\n", clusterinfo.u;

def btfunc_kmeans():
    p = int(clusterinfo.c_p.get());
    terminateturn = int(clusterinfo.c_terminateturn.get());
    dr.drawkmeans(clusterinfo.points, clusterinfo.centroids, p, terminateturn);
    
def btfunc_fcm2():
    m = int(clusterinfo.c_m.get());
    p = int(clusterinfo.c_p.get());
    e = float(clusterinfo.c_e.get());
    terminateturn = int(clusterinfo.c_terminateturn.get());
    dr.drawfcm2(clusterinfo.points, clusterinfo.u, m, p, e, terminateturn);
    
def btfunc_fcm1():
    m = int(clusterinfo.c_m.get());
    p = int(clusterinfo.c_p.get());
    e = float(clusterinfo.c_e.get());
    terminateturn = int(clusterinfo.c_terminateturn.get());
    dr.drawfcm1(clusterinfo.points, clusterinfo.u, m, p, e, terminateturn);
    
"""
------------------------------------------------------------------------
初等函数演示
"""
class ElementaryfuncInfo:
    c_power_a = None;
"""
绘制面板
"""
def createElementaryfuncWidgets(master):
    master.title("elementary function practie");

    r=0;

    tk.Label(master, text="power function parameters").grid(row=r,column=0, sticky=tk.W);
    elementaryfuncinfo.c_power_a = tk.Entry(master, width=100);
    elementaryfuncinfo.c_power_a.insert(0, '-3,-2,-1,-0.5,-0.333333333,0,0.5,0.3333333333,1,2,3');
    elementaryfuncinfo.c_power_a.grid(row=r,column=1);
    tk.Button(master, text="幂函数",width=10, command=btfunc_power).grid(row=r,column=2);

    r=r+1;
    tk.Label(master, text="exponential function parameters").grid(row=r,column=0, sticky=tk.W);
    elementaryfuncinfo.c_exp_a = tk.Entry(master, width=100);
    elementaryfuncinfo.c_exp_a.insert(0, '0.5,0.3333333333,1,2,3');
    elementaryfuncinfo.c_exp_a.grid(row=r,column=1);
    tk.Button(master, text="指数函数",width=10, command=btfunc_exp).grid(row=r,column=2);

    r=r+1;
    tk.Label(master, text="logarithmic function parameters").grid(row=r,column=0, sticky=tk.W);
    elementaryfuncinfo.c_log_a = tk.Entry(master, width=100);
    elementaryfuncinfo.c_log_a.insert(0, '0.5,0.3333333333,2,3');
    elementaryfuncinfo.c_log_a.grid(row=r,column=1);
    tk.Button(master, text="对数函数",width=10, command=btfunc_log).grid(row=r,column=2);

# 幂函数
def btfunc_power():
    print "power function:", elementaryfuncinfo.c_power_a.get(), "\n";
    
    lines=[];
    X=np.linspace(-2,2, 100);
    for sa in elementaryfuncinfo.c_power_a.get().split(','):
        a=float(sa);
        Y=np.power(X, a);
        lines.append((X,Y,sa));
        
    dr.drawlines(lines, "power function");
    
# 指数函数
def btfunc_exp():
    print "exponential function:", elementaryfuncinfo.c_exp_a.get(), "\n";
    
    lines=[];
    X=np.linspace(-2,2, 100);
    for sa in elementaryfuncinfo.c_exp_a.get().split(','):
        a=float(sa);
        Y=np.exp(X*np.log(a));
        lines.append((X,Y,sa));
        
    dr.drawlines(lines, "exponential function");
    
# 对数函数
def btfunc_log():
    print "logarithmic function:", elementaryfuncinfo.c_log_a.get(), "\n";

    lines=[];
    X=np.linspace(0.1,5, 100);
    for sa in elementaryfuncinfo.c_log_a.get().split(','):
        a=float(sa);
        Y=np.log(X)/np.log(a);
        lines.append((X,Y,sa));
        
    dr.drawlines(lines, "logarithmic function");

"""
------------------------------------------------------------------------
main
"""
clusterinfo=ClusterInfo();
elementaryfuncinfo=ElementaryfuncInfo();

# test
def btfunc_test():
    lines=[];
    X=np.linspace(-5,5, 1000);
    Y=np.sinh(X)
    lines.append((X,Y,"y=sinh(x)"));
         
    dr.drawlines(lines, "");


if __name__ == "__main__":
    root = tk.Tk();
    
    tk.Button(root, text="test",width=20, command=btfunc_test).grid(row=0,column=0);
    tk.Button(root, text="cluster",width=20, command=btfunc_cluster).grid(row=1,column=0);
    tk.Button(root, text="elementary function",width=20, command=btfunc_elementaryfunc).grid(row=1,column=1);

    root.title("practie");
    #root.geometry('640x480');

    root.mainloop();
