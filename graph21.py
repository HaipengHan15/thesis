from scipy import integrate
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

def symmetric(a, a_other, size, size_other, num): # N对应a2，M对应a1
    point1 = math.floor(size*num - 1) # 不一定是整数计算对称歧视情况下的收入
    point2 = math.floor(size*num - 1)+3 # 不一定是整数
    v1 = 0
    if num <= 2:
        point2 = num
    base = a*(2*size_other - 1) - 2*a_other*(1-size_other) + 1
    for i1 in range(1, point2+1):
        if i1 <= point1:
            temp = (base - 2 * i1 / num) / num
            v1 += temp
        else:
            temp = (2*size/3 + (4 - 2*i1) / (3*num) -  2*a_other*size_other) * ((2 - i1) / (3*num) + size/3)
            v1 += temp
    return v1

def asymmetric(a, a_other, Pb, na, na_other, nm, NM):
#绘制不对称歧视情况下的利润 N>1, M>1
    result = 0
    base1 = a*(2*na_other - 1) + Pb + 1
    if (nm-2)/NM >= na:
        print('error!')
    for i in range(1, nm+1):
        if i <= nm-2:
            result += (base1 - 2*i/NM) / NM
        else:
            xi = i/(2*NM) + na_1/2 - 1/(4*NM)
            h = (xi - (i-1)/NM)
            if h<0:
                print('error!')
            result += (base1 - 2*xi)*h
    return result

# 0.8, 0.9 for result4.csv
data = pd.read_csv("C:\\Users\\HanHaipeng\\Desktop\\result21.csv")
data.index = ['Pb_1', 'Pb_2', 'na_1', 'na_2', 'n', 'm']
NM = list(data) # 获取data的列名，即所有NM
NM = list(map(int, NM)) # string转int
NM = NM[:8]
alpha1 = 0.2
alpha2 = 0.3
r0 = 1 - (alpha1 + alpha2)/2
profit0 = [r0]*(len(NM)) # 统一定价
profit1 = []
profit2 = [] # 不对称歧视的A平台利润
profit2B = [] # 不对称歧视的B平台利润
for i in NM:
    # print(i)
    temp1 = symmetric(alpha2, alpha1, 0.5, 0.5, i) + symmetric(alpha1, alpha2, 0.5, 0.5, i)
    profit1.append(temp1)

    i_str = str(i)
    Pb_1 = float(data.loc['Pb_1', i_str])
    Pb_2 = float(data.loc['Pb_2', i_str])
    na_1 = float(data.loc['na_1', i_str])
    na_2 = float(data.loc['na_2', i_str])
    n = int(data.loc['n', i_str])
    m = int(data.loc['m', i_str])
    profit2B.append(Pb_1 * (1-na_1) + Pb_2 * (1-na_2))

    temp2 = asymmetric(alpha1, alpha2, Pb_1, na_1, na_2, n, i) + asymmetric(alpha2, alpha1, Pb_2, na_2, na_1, m, i)
    profit2.append(temp2)

plt.plot(NM, profit0, color = 'black')  # 双方都不歧视定价时的利润
plt.plot(NM, profit1, color = 'black')  # 双方都歧视定价时的利润
plt.plot(NM, profit2, color = 'black')  # 另一方不歧视时这一方歧视的利润
plt.plot(NM, profit2B, color = 'black')  # 另一方歧视时这一方不歧视的利润
plt.tick_params(labelsize=20)
plt.xlabel('N and M', fontsize=20)
plt.ylabel('Profits', fontsize=20)
pylab.show()
