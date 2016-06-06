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
        pointscount = self.pointscount.get() or 10;
        if type(pointscount) == str:
            pointscount = int(pointscount);
        points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
        k = self.k.get() or 3;
        if type(k) == str:
            k = int(k);
        centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];
        p = self.p.get() or 2;
        if type(p) == str:
            p = int(p);
        dr.drawkmeans(points, centroids, p);



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
