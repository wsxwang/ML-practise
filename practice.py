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
import Tkinter as tk

import drawgraph as dr


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
        self.c_n = tk.Entry(self.master, width=20);
        self.c_n.insert(0, "100");
        self.c_n.grid(row=2,column=1);
        tk.Label(self.master, text="data points:").grid(row=3,column=0, sticky=tk.W);
        self.c_points = tk.Text(self.master,width=20,height=10);
        self.c_points.grid(row=3,column=1, rowspan=3, columnspan=2);
        tk.Button(self.master, text="random",width=10, command=btfunc_randompoints).grid(row=4,column=0);
        
        tk.Label(self.master, text="Minkowski distance config:").grid(row=1,column=3, sticky=tk.W,columnspan=2);
        tk.Label(self.master, text="p=").grid(row=2,column=3, sticky=tk.W);
        self.c_p = tk.Entry(self.master, width=20);
        self.c_p.insert(0, "2");
        self.c_p.grid(row=2,column=4);
        
        tk.Label(self.master, text="K-means config:").grid(row=10,column=0, sticky=tk.W,columnspan=2);
        tk.Label(self.master, text="k=").grid(row=11,column=0, sticky=tk.W);
        self.c_k = tk.Entry(self.master, width=20);
        self.c_k.insert(0, "3");
        self.c_k.grid(row=11,column=1);
        tk.Label(self.master, text="initial centroids:").grid(row=12,column=0, sticky=tk.W);
        self.c_centroids = tk.Text(self.master,width=20,height=10);
        self.c_centroids.grid(row=12,column=1, rowspan=3, columnspan=2);
        tk.Button(self.master, text="random",width=10, command=btfunc_randomcentroids).grid(row=13,column=0);
        
        tk.Label(self.master, text="fcm config:").grid(row=10,column=3, sticky=tk.W,columnspan=32);
        tk.Label(self.master, text="m=").grid(row=11,column=3, sticky=tk.W);
        self.c_m = tk.Entry(self.master, width=20);
        self.c_m.insert(0, "2");
        self.c_m.grid(row=11,column=4);
        tk.Label(self.master, text="c=").grid(row=12,column=3, sticky=tk.W);
        self.c_c = tk.Entry(self.master, width=20);
        self.c_c.insert(0, "3");
        self.c_c.grid(row=12,column=4);
        tk.Label(self.master, text="ε=").grid(row=13,column=3, sticky=tk.W);
        self.c_e = tk.Entry(self.master, width=20);
        self.c_e.insert(0, "0.001");
        self.c_e.grid(row=13,column=4);
        tk.Label(self.master, text="initial Uij:").grid(row=14,column=3, sticky=tk.W);
        self.c_umatrix = tk.Text(self.master,width=20,height=10);
        self.c_umatrix.grid(row=14,column=4, rowspan=3, columnspan=2);
        tk.Button(self.master, text="random",width=10, command=btfunc_randomumatrix).grid(row=15,column=3);

"""
------------------------------------------------------------------------
功能函数
"""
def strorint(si):
    if type(si) == str:
        si = int(si);
    return si;

"""
------------------------------------------------------------------------
按钮函数
"""
# 按钮函数
def btfunc_randompoints():
    pointscount = strorint(config.c_n.get());
    main.points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
    print main.points;

def btfunc_randomcentroids():
    k = strorint(config.c_k.get());
    main.centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
    print main.centroids;

def btfunc_randomumatrix():
    c = strorint(config.c_c.get());
    pointscount = strorint(config.c_n.get());
    main.u = [[0 for j in range(c)] for i in range(pointscount)];
    for i in range(pointscount):
        for j in range(c-1):
            leftrange = c-sum(main.u[i])-1;
            if leftrange == 0:
                break;
            main.u[i][j] = random.randint(0, leftrange);
        if sum(main.u[i]) == 0:
            main.u[i][0] = 1;
        main.u[i][c-1] = c-sum(main.u[i]);
    main.u = np.dot(main.u, 1/float(c));
    print main.u[i];
        #    main.u[i][j] = random.randint(0, c-sum(main.u[i])-1)/float(c);
        #main.u[i][c-1] = 1-sum(u[i]);
    print main.u;

def btfunc_kmeans():
    p = strorint(config.c_p.get());
    dr.drawkmeans(main.points, main.centroids, p);
    
def btfunc_fcm():
    m = strorint(config.c_m.get());
    p = strorint(config.c_p.get());
    e = float(config.c_e.get());
    dr.drawfcm2(main.points, main.u, m, p, e);

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

        tk.Button(self.root, text="k-means",width=10, command=btfunc_kmeans).grid(row=0,column=0);
        tk.Button(self.root, text="fcm", width=10, command=btfunc_fcm).grid(row=0,column=1);

        config.createWidgets();
        btfunc_randompoints();
        btfunc_randomcentroids();
        btfunc_randomumatrix();

        self.root.mainloop();
        
main = ClassMain();
config = FrmConfig(main.root);

if __name__ == "__main__":
    main.mainfunc();

    
