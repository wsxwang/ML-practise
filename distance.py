#-*-coding:utf-8-*-

"""
distance.py
Wang Xiaoqi
create:2016-05-18

calculate distance bwteen two points
distance type:minkowsky distance, euclidean distance,manhattan distance

求解两点距离
"""

import sys;
import os;

"""
calculate minkowsky distance
P,Q:two vectors(list), same dimension

计算闵氏距离
P,Q是两个同维向量
"""
def minkowsky_dis(P,Q,p):
    assert(len(P) == len(Q));
    return 0;


if __name__ == "__main__":
    P = [3,0];
    Q = [0,4];
    assert(minkowsky_dis(P, Q, 2) == 5);

