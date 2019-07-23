import numpy as np
from openpyxl import load_workbook
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
import base1

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

def location(x, N):
    # 0 <= x <= 1
    for i in range(1, N+1):
        if x >= (i-1)/N and x < i/N:
            return i
    if x == 1:
        return N

def utility(x, N, alpha1, alpha2, value1, value2):
    i = location(x, N)
    if i/N <= (alpha2+1)/2 - 1/N:
        return value1 + 0.5*alpha1 - 1 + 2*i/N - x
    elif i/N <= (3*alpha2+1)/2 - 1/N:
        return value1 + 0.5*alpha1 - 0.5 + (i-1)/N + alpha2/2 - x
    elif i/N < (1 - 3*alpha2)/2 + 2/N:
        return value1 + 0.5*alpha1 - (N-2*i+4)/(3*N) + alpha2 - x
    elif i/N < (1 - alpha2)/2 + 2/N:
        return 0 # value1 + 0.5*alpha1 - x
    else:
        return 0

x = np.linspace(0, 0.6, 1000)
y = np.array([utility(t, 20, 0.04, 0.04, 1, 1) for t in x])

plt.figure()
plt.scatter(x, y, s=0.1)
#plt.ylim(-0.1, 1.2)   #限制y的范围
plt.show()