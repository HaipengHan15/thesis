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

NM = np.arange(1, 25, 2)
a1 = 0.01
a2 = 2

# 假设N和M同步增长，计算总收入
# 对称歧视情况下
ipoint1 = NM / 2 - 1
ipoint2 = 2 + NM / 2 + 3 * NM * a2 * (NM * (1 - a2 - 3 * a1) - 1) / 8
jpoint1 = NM * (a1 + a2) / 2 - 1
jpoint2 = NM * (a2 - a1) / 2 + 1
r = [(a2**2 - a1**2) / 16]
r_1 = [0]
r_2 = [(a2**2 - a1**2) / 16]
r0 = [r[0]]

for i in range(1, len(NM)):
    if NM[i] < 1 / (a1 + a2 - 1):  # 回退到single-homing
        base = base1.base1(a1, a2, NM, NM)
        r.append(base.Group1[1][i] + base.Group2[1][i])
        r0.append(r0[0])
        print("h")
    else:
        iv1 = 0
        iv2 = 0
        jv1 = 0
        jv2 = 0
        i1 = 1
        j1 = 1
        # 计算group-1的收入
        while i1 <= ipoint1[i]:
            temp = (1 - 2 * i1 / NM[i]) / NM[i]
            if(temp < 0):
                print("1", i1, ipoint1[i], NM[i])
            iv1 += temp
            i1 += 1
        # 计算group-2的收入
        if(a1 + a2 < 1 + 3 / NM[i]):
            while j1 < jpoint1[i]:
                temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
                if(temp < 0):
                    print("4", j1, jpoint1[i], NM[i])
                jv1 += temp
                j1 += 1
            while j1 <= jpoint2[i]:
                temp = ((a2 - a1) / 4 - (j1 - 1) /
                        (2 * NM[i])) * ((a2 + a1) / 4 - (j1 - 1) / (2 * NM[i]))
                if(temp < 0):
                    print("5", j1, jpoint2[i], NM[i])
                jv2 += temp
                j1 += 1
        else:
            while j1 < NM[i] + 1:
                temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
                if(temp < 0):
                    temp = 0
                #print("6", NM[i])
                jv1 += temp
                j1 += 1
        #print(iv1, iv2, jv1, jv2)
        r.append(iv1 + iv2 + jv1 + jv2)
        r_1.append(iv1 + iv2)
        r_2.append(jv1 + jv2)
        r0.append(r0[0])

# 绘制不对称歧视情况下的利润
ipoint1 = (NM - 1) / 2
ipoint2 = 1.5 + NM / 2 + (NM**2) * a2 * (1 - a2 - 3 * a1) / 4 - NM * a2 / 4
jpoint1 = NM * (a1 + a2) / 2 - 1
jpoint2 = NM * (a2 - a1) / 2 + 1
r2 = [r[0]]
r2_1 = [r_1[0]]
r2_2 = [r_2[0]]
r2B = [r[0]]  # 不分段
pB1 = NM * a2 * (1 - a2 - 3 * a1) / 4 - a2 / 4 + 1 / NM
pB2 = (a2 - a1 - 1) / 4 + 1 / (4 * NM)

for i in range(len(NM)):
    if pB1[i] < 0:
        pB1[i] = 0
    if pB2[i] < 0:
        pB2[i] = 0

for i in range(1, len(NM)):
    iv1 = 0
    iv2 = 0
    jv1 = 0
    jv2 = 0
    i1 = 1
    j1 = 1
    nB1 = 0.5
    nB2 = (1 + (a2 + a1 - 1) * NM[i]) / 4
    # 计算group-1的收入
    while i1 < ipoint1[i]:
        temp = (1 - 2 * i1 / NM[i]) / NM[i]
        if(temp < 0):
            print("6", i1, ipoint1[i], NM[i])
        iv1 += temp
        i1 += 1
    # 计算group-2的收入
    if(a1 + a2 < 1 + 3 / NM[i]):
        while j1 < jpoint1[i]:
            temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
            if(temp < 0):
                print("7", j1, jpoint1[i], NM[i])
            jv1 += temp
            j1 += 1
        while j1 <= jpoint2[i]:
            temp = ((a2 - a1) / 4 - (j1 - 1) /
                    (2 * NM[i])) * ((a2 + a1) / 4 - (j1 - 1) / (2 * NM[i]))
            if(temp < 0):
                print("8", j1, jpoint2[i], NM[i])
            jv2 += temp
            j1 += 1
    else:
        nB2 = 1
        while j1 < NM[i] + 1:
            temp = (0.5 * a2 - j1 / NM[i]) / NM[i]
            if(temp < 0):
                temp = 0
            # print("6", NM[i])
            jv1 += temp
            j1 += 1
    r2.append(iv1 + iv2 + jv1 + jv2)
    r2_1.append(iv1 + iv2)
    r2_2.append(jv1 + jv2)
    r2B.append(pB2[i] * nB2)

result0 = np.array(r0)
result = np.array(r)
result_1 = np.array(r_1)
result_2 = np.array(r_2)
result2 = np.array(r2)
result2_1 = np.array(r2_1)
result2_2 = np.array(r2_2)
result2B = np.array(r2B)

# print(result)

plt.plot(NM, result0)  # 双方都不歧视定价时的利润
plt.plot(NM, result)  # 双方都歧视定价时的利润
plt.plot(NM, result_1)
plt.plot(NM, result_2)
plt.plot(NM, result2)  # 另一方不歧视时这一方歧视的利润
plt.plot(NM, result2_1)
plt.plot(NM, result2_2)
plt.plot(NM, result2B)  # 另一方歧视时这一方不歧视的利润
plt.xlabel('N/M', fontsize=12)
plt.ylabel(u'利润', fontsize=12)
pylab.show()
