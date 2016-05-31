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

from kmeans import *


"""
------------------------------------------------------------------------
K-means test
"""
class CKmeans():
    def __init__(self, master):
        self.master = master;

    def createWidgets(self):
        l=tk.Label(self.master, text="k=");
        l.pack();
        l.place(x=10, y= 10);
        self.k = tk.Entry(self.master);
        self.k.pack();
        self.k.place(x=100, y=10);
        
        l=tk.Label(self.master, text="p=");
        l.pack();
        l.place(x=10, y= 40);
        self.p = tk.Entry(self.master);
        self.p.pack();
        self.p.place(x=100, y=40);
        
        l=tk.Label(self.master, text="point count=");
        l.pack();
        l.place(x=10, y= 70);
        self.pointscount = tk.Entry(self.master);
        self.pointscount.pack();
        self.pointscount.place(x=100, y=70);

        bt = tk.Button(self.master, text='k-means', command=self.btfunc_kmeans);
        bt.pack();
        bt.place(x=100, y=100);

        
    def btfunc_kmeans(self):
        self.do_kmeans(self.pointscount.get() or 10, self.k.get() or 3, self.p.get() or 2);

    def do_kmeans(self, pointscount, k, p):
        if type(pointscount) == str:
            pointscount = int(pointscount);
        if type(p) == str:
            p = int(p);
        if type(k) == str:
            k = int(k);
        
        plt.figure(figsize=(8,8), dpi=80);
        plt.xlabel("X");
        plt.ylabel("Y");
        plt.ylim(-1,1)
        plt.title("k-means, %d points, k=%d, p=%d"%(pointscount,k,p));
        plt.plot(np.linspace(-100, 100, 100), np.zeros(100), "k,", linewidth = 2);
        plt.plot(np.zeros(100), np.linspace(-100, 100, 100), "k,", linewidth = 2);

        points=[[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
        centroids=[[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
        print points;
        print centroids;
        clusters=alg_kmeans(points, centroids, p);
                            

        
        plt.legend();
        plt.show();

"""
------------------------------------------------------------------------
main
"""
if __name__ == "__main__":
    root = tk.Tk();
    root.title("practie");
    root.geometry('640x480');

    kmeans = CKmeans(root);
    kmeans.createWidgets();

    root.mainloop();
