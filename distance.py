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
import numpy as np;

"""
calculate minkowsky distance
P,Q:two vectors(list), same dimension

计算闵氏距离
P,Q是两个同维向量
"""
def dis_minkowski(P,Q,p):
    assert(len(P) == len(Q));
    dp = 0;
    for i in range(0, len(P)):
        dp += np.power(np.abs(P[i] - Q[i]), p);
    return np.power(dp, 1/float(p));


"""
------------------------------------------------------------------------
test function
"""
def test_minkowski():
    P = [4,2];
    Q = [1,6];
    assert(dis_minkowski(P, Q, 2) == 5);

    P = [1,0];
    Q = [0,1];
    assert(dis_minkowski(P, Q, 4) == np.power(2, 0.25));

    P = [0,1,2];
    Q = [1,2,3];
    assert(dis_minkowski(P,Q,3) == np.power(3, 1/float(3)));
    
    P = [0,1,2];
    Q = [1,2,3];
    assert(dis_minkowski(P,Q,10) == np.power(3, 0.1));
    
    P = [0,1,2];
    Q = [1,2,3];
    assert(dis_minkowski(P,Q,0.5) == np.power(3, 2));
    
if __name__ == "__main__":
    test_minkowski();

           
    

