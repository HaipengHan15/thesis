from scipy import integrate
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

def symmetric(num, a): # N对应a2，M对应a1
    point1 = (num - 2) / 2 # 不一定是整数计算对称歧视情况下的收入
    point2 = math.floor((num + 3) / 2) # 不一定是整数
    v1 = 0
    if num==1:
        point2 = 1
    for i1 in range(1, point2+1):
        if i1 <= point1:
            temp = (1 - 2 * i1 / num -  a) / num
            v1 += temp
        else:
            temp = (1/3 + (4 - 2*i1) / (3*num) -  a) * ((2 - i1) / (3*num) + 1/6)
            v1 += temp
    return v1

def asymmetric(a1, a2, Pb_1, Pb_2, na_1, na_2, n, m, N, M):
#绘制不对称歧视情况下的利润 N>1, M>1
    result = 0
    base1 = a1*(2*na_2 - 1) + Pb_1 + 1
    base2 = a2*(2*na_1 - 1) + Pb_2 + 1
    if (n-2)/N >= na_1 or (m-2)/M >= na_2:
        print('error!')
    for i in range(1, n+1):
        if i <= n-2:
            result += (base1 - 2*i/N) / N
        else:
            xi = i/(2*N) + na_1/2 - 1/(4*N)
            h = (xi - (i-1)/N)
            if h<0:
                print('error!')
            result += (base1 - 2*xi)*h
    for j in range(1, m+1):
        if j <= m - 2:
            result += (base2 - 2*j/M) / M
        else:
            yj = j/(2*M) + na_2/2 - 1/(4*M)
            g = (yj - (j - 1)/M)
            if g<0:
                print('error!')
            result += (base2 - 2*yj)*g
    return result

data = pd.read_csv("C:\\Users\\HanHaipeng\\Desktop\\result21.csv")
data.index = ['Pb_1', 'Pb_2', 'na_1', 'na_2', 'n', 'm']
NM = list(data) # 获取data的列名，即所有NM
NM = list(map(int, NM)) # string转int
alpha1 = 0.2
alpha2 = 0.3
r0 = 1 - (alpha1 + alpha2)/2
profit0 = [r0]*(data.shape[1]) # 统一定价
profit1 = []
profit2 = [] # 不对称歧视的A平台利润
profit2B = [] # 不对称歧视的B平台利润
for i in NM:
    # print(i)
    temp1 = symmetric(i, alpha2) + symmetric(i, alpha1)
    profit1.append(temp1)

    i_str = str(i)
    Pb_1 = float(data.loc['Pb_1', i_str])
    Pb_2 = float(data.loc['Pb_2', i_str])
    na_1 = float(data.loc['na_1', i_str])
    na_2 = float(data.loc['na_2', i_str])
    n = int(data.loc['n', i_str])
    m = int(data.loc['m', i_str])
    profit2B.append(Pb_1 * (1-na_1) + Pb_2 * (1-na_2))

    temp2 = asymmetric(alpha1, alpha2, Pb_1, Pb_2, na_1, na_2, n, m, i, i)
    profit2.append(temp2)

plt.plot(NM, profit0, color = 'black')  # 双方都不歧视定价时的利润
plt.plot(NM, profit1, color = 'black')  # 双方都歧视定价时的利润
plt.plot(NM, profit2, color = 'black')  # 另一方不歧视时这一方歧视的利润
plt.plot(NM, profit2B, color = 'black')  # 另一方歧视时这一方不歧视的利润
plt.xlabel('N and M', fontsize=12)
plt.ylabel('Profits', fontsize=12)
pylab.show()
