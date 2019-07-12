from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline


class base1:
    # 分别计算单边的收入
    # 系数a指的是另外一边的系数

    def __init__(self, a1, a2, N, M):
        self.a1 = a1
        self.a2 = a2
        self.N = N
        self.M = M
        self.Group1 = [np.zeros(len(N))] * 4
        self.Group2 = [np.zeros(len(M))] * 4

        if a2 >= 1 and a1 >= 1:
            pass
        elif a2 < 1 and a1 >= 1:
            self.Group1 = self.singleIncome(N)
        elif a2 >= 1 and a1 < 1:
            self.Group2 = self.singleIncome(M)
        else:
            self.Group1 = self.doubleIncome(N, self.a2)
            self.Group2 = self.doubleIncome(M, self.a1)

    def singleIncome(self, num):
        point1 = (num - 2) / 2
        point2 = (num + 4) / 2
        point21 = (num - 1) / 2
        point22 = (num + 3) / 2
        r0 = [0.5]
        r = [0.5]
        r2 = [0.5]
        r2B = [0.5]
        # 计算对称歧视情况下的收入
        for i in range(1, len(num)):
            v1 = 0
            v2 = 0
            i1 = 1
            while i1 < point1[i]:
                temp = (1 - 2 * i1 / num[i]) / num[i]
                if(temp < 0):
                    print(i1, point1[i], temp)
                v1 += temp
                i1 += 1
            while i1 <= point2[i]:
                temp = (1 / 3 + (4 - 2 * i1) / (3 * num[i])) * \
                    (1 / 6 - (i1 - 2) / (3 * num[i]))
                if(temp < 0):
                    print(i1, point2[i], temp)
                v2 += temp
                i1 += 1
            r0.append(r0[0])
            r.append(v1 + v2)
        # 计算不对称歧视情况下的收入
        for i in range(1, len(num)):
            v1 = 0
            v2 = 0
            i1 = 1
            while i1 < point21[i]:
                temp = (1 - (2 * i1 - 1) / num[i]) / num[i]
                if(temp < 0):
                    print(i1, point21[i], temp)
                v1 += temp
                i1 += 1
            while i1 <= point22[i]:
                temp = ((num[i] - 2 * i1 + 3) / (2 * num[i])) * \
                    (1 / 4 - (2 * i1 - 3) / (4 * num[i]))
                if(temp < 0):
                    print(i1, point22[i], temp)
                v2 += temp
                i1 += 1
            r2.append(v1 + v2)
            r2B.append(1 / (2 * num[i]))
        group = [np.array(r0), np.array(r), np.array(r2), np.array(r2B)]
        return group

    def doubleIncome(self, num, a):
        point1 = num * (a + 2) / 4 - 1
        point2 = (3 * a + 1) * num / 2 - 1
        # 计算对称歧视情况下的收入
        point3 = (1 - 3 * a) * num / 2 + 2
        r0 = [0.5 * (1 - a)]
        r = [r0[0]]  # 不分段
        for i in range(1, len(num)):
            v1 = 0
            v2 = 0
            v3 = 0
            i1 = 1
            while i1 <= point1[i]:
                temp = (1 - 2 * i1 / num[i]) / num[i]
                if(temp < 0):
                    print(i1, point1[i], temp)
                v1 += temp
                i1 += 1
            while i1 <= point2[i]:
                temp = (1 - 2 * i1 / num[i]) / num[i]
                #temp = (0.5 - (i1 - 1) / num[i] - a / 4) * \
                #    (0.25 + a / 8 - (i1 - 1) / (2 * num[i]))
                if(temp < 0):
                    print(i1, point2[i], temp)
                v2 += temp
                i1 += 1
            while i1 <= point3[i]:
                temp = ((num[i] - 2 * i1 + 4) / (3 * num[i]) - a) * \
                    (1 / 6 - (i1 - 2) / (3 * num[i]))
                if(temp < 0):
                    print(i1, point3[i], temp)
                v3 += temp
                i1 += 1
            r0.append(r0[0])
            r.append(v1 + v2 + v3)

        # 绘制不对称歧视情况下的利润
        point1 = (num - 1) / 2
        point2 = (0.5 - a) * num + 3 / 2
        r2 = [0.5 - 0.5 * a]
        r2B = [r2[0]]  # 不分段

        for i in range(1, len(num)):
            v1 = 0
            v2 = 0
            i1 = 1
            while i1 <= point1[i]:
                temp = (1 - (2 * i1 - 1) / num[i] - a) / num[i]
                if(temp < 0):
                    print("4", i1, point1[i], temp)
                v1 += temp
                i1 += 1
            while i1 < point2[i]:
                temp = (((num[i] - 2 * i1 + 3) / (2 * num[i])) - a) * \
                    (1 / 4 - (2 * i1 - 3) / (4 * num[i]))
                if(temp < 0):
                    print("5", i1, point2[i], temp)
                v2 += temp
                i1 += 1
            r2.append(v1 + v2)
            r2B.append(1 / (2 * num[i]) - a / 2)
        group = [np.array(r0), np.array(r), np.array(r2), np.array(r2B)]
        return group
