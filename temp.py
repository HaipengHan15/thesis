from scipy import integrate
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

# pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
# font1 = {'family': 'Times New Roman',
#          'weight': 'normal',
#          'size': 23,
#          }

def symmetric(num):
    point1 = num/2 - 1 # 不一定是整数计算对称歧视情况下的收入
    point2 = math.floor(num/2 + 3/2) # 不一定是整数
    v1 = 0
    if num <= 2:
        point2 = num
    for i1 in range(1, point2+1):
        if i1 <= point1:
            temp = (1 - 2 * i1 / num) / num
            v1 += temp
        else:
            temp = (1/3 + (4 - 2*i1) / (3*num)) * ((2 - i1) / (3*num) + 1/6)
            v1 += temp
    return v1

def asymmetric(Pb, na, nm, NM):
    result = 0
    base1 = Pb + 1
    if (nm-2)/NM >= na:
        print('error!')
    for i in range(1, nm+1):
        if i <= nm-2:
            result += (base1 - 2*i/NM) / NM
        else:
            xi = i/(2*NM) + na/2 - 1/(4*NM)
            h = (xi - (i-1)/NM)
            if h<0:
                print('error!')
            result += (base1 - 2*xi)*h
    return result

data = pd.read_csv("C:\\Users\\HanHaipeng\\Desktop\\temp.csv")
flag = 50 # data.shape[1]
NM = range(1, flag + 1)
# print(data.shape[1])
profit0 = [0.5]*(flag) # 统一定价
profit1 = [] # 对称歧视的企业利润
profit2 = [] # 不对称歧视的企业1利润
profit2B = data.iloc[1].tolist() # 不对称歧视的企业2利润
for i in range(flag):
    # print(i)
    temp1 = symmetric(i+1)
    profit1.append(temp1)
    Pb_1 = float(data.iloc[0, i])
    na_1 = 1 - float(data.iloc[2, i])
    n = int(data.iloc[3, i])
    temp2 = asymmetric(Pb_1, na_1, n, i+1)
    profit2.append(temp2)
# plt.plot(NM, data.loc[0].tolist(), color = 'red') 
plt.plot(NM, profit0, color = 'black') # 双方都统一定价时的利润
plt.plot(NM, profit1, color = 'black')  # 双方都歧视定价时的利润
plt.plot(NM, profit2B[0: flag], color = 'black') # 另一方不歧视时这一方歧视的利润
plt.plot(NM, profit2, color = 'black')# 另一方歧视时这一方不歧视的利润
# plt.plot(NM, data.iloc[2].tolist(), color = 'blue')
# plt.plot(NM, data.iloc[3].tolist(), color = 'black')
plt.xlabel('N', fontsize=12)
plt.ylabel('Profits', fontsize=12)
pylab.show()
# for i in range(flag-1):
#     if profit1[i+1] >= profit1[i]:
#         print(i)