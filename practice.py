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

from kmeans import *
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.km_pInput = Entry(self)
        self.km_pInput.pack()
        self.km_pointsInput = Entry(self)
        self.km_pointsInput.pack()
        self.km_Button = Button(self, text='k-means', command=self.kmeans)
        self.km_Button.pack()

    def kmeans(self):
        test_kmeans(self.km_pointsInput.get() or 10, self.km_pInput.get() or 2);

"""
------------------------------------------------------------------------
test function
"""

"""
k-means test function
"""
def test_kmeans(pointscount, p):
    if type(pointscount) == str:
        pointscount = int(pointscount);
    if type(p) == str:
        p = int(p);
    
    plt.figure(figsize=(8,8), dpi=80);
    plt.xlabel("X");
    plt.ylabel("Y");
    plt.ylim(-1,1)
    plt.title("k-means, %d points, p = %d"%(pointscount,p));

    plt.plot(np.linspace(-1, 1, 100), np.zeros(100), "k,", linewidth = 2);
    plt.plot(np.zeros(100), np.linspace(-1, 1, 100), "k,", linewidth = 2);
    plt.legend();
    plt.show();
    
if __name__ == "__main__":
    app = Application();
    app.master.title('hello');
    app.mainloop();
    
