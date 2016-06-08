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
------------------------------------------------------------------------
配置界面
"""
class FrmConfig():
    def __init__(self, master):
        self.master = master;

    def createWidgets(self):
        tk.Label(self.master, text="data point set config:").grid(row=1,column=0, sticky=tk.W,columnspan=2);
        tk.Label(self.master, text="n=").grid(row=2,column=0, sticky=tk.W);
        self.c_n = tk.Entry(self.master, width=10);
        self.c_n.insert(0, "100");
        self.c_n.grid(row=2,column=1);
        tk.Label(self.master, text="data points:").grid(row=3,column=0, sticky=tk.W);
        tk.Button(self.master, text="random",width=10, command=btfunc_randompoints).grid(row=3,column=1);
        
        tk.Label(self.master, text="Minkowski distance config:").grid(row=1,column=3, sticky=tk.W,columnspan=2);
        tk.Label(self.master, text="p=").grid(row=2,column=3, sticky=tk.W);
        self.c_p = tk.Entry(self.master, width=10);
        self.c_p.insert(0, "2");
        self.c_p.grid(row=2,column=4);
        
        tk.Label(self.master, text="K-means config:").grid(row=10,column=0, sticky=tk.W,columnspan=2);
        tk.Label(self.master, text="k=").grid(row=11,column=0, sticky=tk.W);
        self.c_k = tk.Entry(self.master, width=10);
        self.c_k.insert(0, "3");
        self.c_k.grid(row=11,column=1);
        tk.Label(self.master, text="initial centroids:").grid(row=12,column=0, sticky=tk.W);
        tk.Button(self.master, text="random",width=10, command=btfunc_randomcentroids).grid(row=12,column=1);
        
        tk.Label(self.master, text="fcm config:").grid(row=10,column=3, sticky=tk.W,columnspan=32);
        tk.Label(self.master, text="m=").grid(row=11,column=3, sticky=tk.W);
        self.c_m = tk.Entry(self.master, width=10);
        self.c_m.insert(0, "2");
        self.c_m.grid(row=11,column=4);
        tk.Label(self.master, text="c=").grid(row=12,column=3, sticky=tk.W);
        self.c_c = tk.Entry(self.master, width=10);
        self.c_c.insert(0, "3");
        self.c_c.grid(row=12,column=4);
        tk.Label(self.master, text="ε=").grid(row=13,column=3, sticky=tk.W);
        self.c_e = tk.Entry(self.master, width=10);
        self.c_e.insert(0, "0.001");
        self.c_e.grid(row=13,column=4);
        tk.Label(self.master, text="initial Uij:").grid(row=14,column=3, sticky=tk.W);
        tk.Button(self.master, text="random",width=10, command=btfunc_randomumatrix).grid(row=14,column=4);

"""
------------------------------------------------------------------------
按钮函数
"""
# 按钮函数
def btfunc_randompoints():
    pointscount = int(config.c_n.get());
    main.points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
    print "random points:\n", main.points;

def btfunc_randomcentroids():
    k = int(config.c_k.get());
    main.centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
    print "random centroids:\n", main.centroids;

def btfunc_randomumatrix():
    c = int(config.c_c.get());
    pointscount = int(config.c_n.get());
    main.u = [[0 for j in range(c)] for i in range(pointscount)];
    for i in range(pointscount):
        for j in range(c-1):
            leftrange = c*10-sum(main.u[i])-1;
            if leftrange == 0:
                break;
            main.u[i][j] = random.randint(0, leftrange);
        if sum(main.u[i]) == 0:
            main.u[i][0] = 1;
        main.u[i][c-1] = c*10-sum(main.u[i]);
    main.u = np.dot(main.u, 1/float(c*10));
    print "random Uij:\n", main.u;

def btfunc_kmeans():
    p = int(config.c_p.get());
    terminateturn = int(main.c_terminateturn.get());
    dr.drawkmeans(main.points, main.centroids, p, terminateturn);
    
def btfunc_fcm2():
    m = int(config.c_m.get());
    p = int(config.c_p.get());
    e = float(config.c_e.get());
    terminateturn = int(main.c_terminateturn.get());
    dr.drawfcm2(main.points, main.u, m, p, e, terminateturn);
    
def btfunc_fcm1():
    m = int(config.c_m.get());
    p = int(config.c_p.get());
    e = float(config.c_e.get());
    terminateturn = int(main.c_terminateturn.get());
    dr.drawfcm1(main.points, main.u, m, p, e, terminateturn);

"""
------------------------------------------------------------------------
main
"""
class ClassMain():
    root = tk.Tk();
    points = None;
    centroids = None;
    u = None;

    def mainfunc(self):
        self.root.title("practie");
        #root.geometry('640x480');

        tk.Label(self.root, text="terminate turn=").grid(row=0,column=0, sticky=tk.W);
        self.c_terminateturn = tk.Entry(self.root, width=10);
        self.c_terminateturn.insert(0, str(sys.maxint));
        self.c_terminateturn.grid(row=0,column=1);
        tk.Button(self.root, text="k-means",width=10, command=btfunc_kmeans).grid(row=0,column=2);
        tk.Button(self.root, text="fcm2", width=10, command=btfunc_fcm2).grid(row=0,column=3);
        tk.Button(self.root, text="fcm1", width=10, command=btfunc_fcm1).grid(row=0,column=4);

        config.createWidgets();
        btfunc_randompoints();
        btfunc_randomcentroids();
        btfunc_randomumatrix();

        self.root.mainloop();
        
main = ClassMain();
config = FrmConfig(main.root);

if __name__ == "__main__":
    main.mainfunc();
