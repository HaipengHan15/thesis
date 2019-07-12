from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
import base1

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

N = np.arange(1, 25)
M = np.arange(1, 25)
base = base1.base1(0.04, 0.02, N, M)
group1_result0 = base.Group1[0]
group1_result = base.Group1[1]
group1_result2 = base.Group1[2]
group1_result2B = base.Group1[3]
plt.plot(N, group1_result0)  # 双方都不歧视定价时的利润
plt.plot(N, group1_result)  # 双方都歧视定价时的利润
plt.plot(N, group1_result2)  # 另一方不歧视时这一方歧视的利润
plt.plot(N, group1_result2B)  # 另一方歧视时这一方不歧视的利润
plt.xlabel('N', fontsize=12)
plt.ylabel(u'利润', fontsize=12)
pylab.show()
