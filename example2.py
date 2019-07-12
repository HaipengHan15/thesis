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

NM = np.arange(1, 25)
a2 = 1.5

# 假设N=1，考虑group-2的收入
# 对称歧视情况下
jpoint1 = NM * a2 / 2 - 1
jpoint2 = NM * a2 / 2 + 1
r = [a2**2 / 16]
r0 = [r[0]]

for i in range(1, len(NM)):
    jv1 = 0
    jv2 = 0
    j1 = 1
    # 计算group-2的收入
    while j1 < jpoint1[i]:
        temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
        if(temp < 0):
            print("1", j1, jpoint1[i], NM[i])
        jv1 += temp
        j1 += 1
    while j1 < jpoint2[i]:
        temp = (a2 / 4 - (j1 - 1) /
                (2 * NM[i])) * (a2 / 4 - (j1 - 1) / (2 * NM[i]))
        if(temp < 0):
            print("2", j1, jpoint2[i], NM[i])
        jv2 += temp
        j1 += 1
    r.append(jv1 + jv2)
    r0.append(r0[0])

# 绘制不对称歧视情况下的利润
jpoint1 = NM * a2 / 2 - 1
jpoint2 = NM * a2 / 2 + 1
r2 = [r[0]]
r2B = [r[0]]
pB2 = (a2 - 1) / 4 + 1 / (4 * NM)

for i in range(1, len(NM)):
    jv1 = 0
    jv2 = 0
    j1 = 1
    nA1 = 0
    # 计算group-2的收入
    while j1 < jpoint1[i]:
        temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
        if(temp < 0):
            print("3", j1, jpoint1[i], NM[i])
        jv1 += temp
        j1 += 1
        nA1 += 1 / NM[i]
        #if(NM[i]==2): print('j1', nA1)
    while j1 < jpoint2[i]:
        temp = (a2 / 4 - (j1 - 1) /
                (2 * NM[i])) * (a2 / 4 - (j1 - 1) / (2 * NM[i]))
        if(temp < 0):
            print("4", j1, jpoint2[i], NM[i])
        jv2 += temp
        j1 += 1
        nA1 += (a2 / 4 - (j1 - 1) / (2 * NM[i]))
        #if(NM[i]==2): print('j2', nA1, j1, jpoint2[i])
    # if(nA1 < 0.5):
    # print(NM[i])
    # r2.append(base1.base1(0.1, 2, NM, NM).Group2[2][i])
    # r2B.append(base1.base1(0.1, 2, NM, NM).Group2[3][i])
    # else:
    r2.append(jv1 + jv2)
    r2B.append(pB2[i] * nA1)
    print(NM[i], nA1, pB2[i] * nA1)

result0 = np.array(r0)
result = np.array(r)
result2 = np.array(r2)
result2B = np.array(r2B)

plt.plot(NM, result0)  # 双方都歧视定价时的利润
plt.plot(NM, result)  # 双方都不歧视定价时的利润
plt.plot(NM, result2)  # 另一方不歧视时这一方歧视的利润
plt.plot(NM, result2B)  # 另一方歧视时这一方不歧视的利润
plt.xlabel('M', fontsize=12)
plt.ylabel(u'利润', fontsize=12)
pylab.show()
