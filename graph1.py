from scipy import integrate
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
# import base3

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }


data = pd.read_csv("C:\\Users\\HanHaipeng\\Desktop\\result3.csv")
# N = 500
# M = 500
# alpha1 = 0.2
# alpha2 = 0.3
# base = base3.base3(alpha1, alpha2, N, M)
# r0 = base.symmetric(0, alpha2) + base.symmetric(0, alpha1)
# group1_result0 = [r0]*N
# group1_result = [r0]
# group1_result2 = [r0]
# group1_result2B = [r0]
# for i in range(1, N):
#     group1_result.append(base.Group[0][i][i])
#     group1_result2.append(base.Group[1][i][i])
#     group1_result2B.append(base.Group[2][i][i])
# axis = range(1, N+1)
# plt.plot(axis, group1_result0)  # 双方都不歧视定价时的利润
# plt.plot(axis, group1_result)  # 双方都歧视定价时的利润
# plt.plot(axis, group1_result2)  # 另一方不歧视时这一方歧视的利润
# plt.plot(axis, group1_result2B)  # 另一方歧视时这一方不歧视的利润
# plt.xlabel('N', fontsize=12)
# plt.ylabel(u'利润', fontsize=12)
# pylab.show()
