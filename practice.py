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


def strorint(si):
    if type(si) == str:
        si = int(si);
    return si;

"""
------------------------------------------------------------------------
main
"""
#控件
root = tk.Tk();             # form
e_n = tk.Entry(root, text="100");       # data count
t_points = tk.Text(root, width=30, height=10
                   ,wrap='none');   # data points

        
# 按钮函数
def btfunc_randompoints():
    pass;

def btfunc_kmeans():
    pointscount = strorint(e_n.get() or 10);
    k = 3;
    p = 2;
    
    points = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(pointscount)];
    centroids = [[random.randint(-100, 100), random.randint(-100, 100)] for i in range(k)];

    dr.drawkmeans(points, centroids, p);
    
    
if __name__ == "__main__":
    root.title("practie");
    root.geometry('640x480');

    # data config
    l=tk.Label(root, text="data point set config:");
    l.pack();
    l.place(x=10,y=10);
    l=tk.Label(root, text="n=");
    l.pack();
    l.place(x=10, y= 40);
    e_n.pack();
    e_n.place(x=50, y=40);
    l=tk.Label(root, text="points:");
    l.pack();
    l.place(x=10, y=80);
    bt=tk.Button(root, text='random data', command=btfunc_randompoints);
    bt.pack();
    bt.place(x=80, y=80);
    t_points.pack();
    t_points.place(x=10, y=120);

    # draw k-means gragh
    bt=tk.Button(root, text='k-means', command=btfunc_kmeans);
    bt.pack();
    bt.place(x=80, y=80);



    root.mainloop();

    #

"""
    # data points
    e_points.pack();
    e_points.place(x=200,y=10);

    f = tk.Toplevel(root);
    f.title("nwe");
    tk.Label(f, text="new").pack();
    f.mainloop();
        


    

    #kmeans = CKmeans(root);
    #kmeans.createWidgets();
"""
    
