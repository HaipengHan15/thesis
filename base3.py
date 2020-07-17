from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import math

class base3:
    # 分别计算单边的收入
    # 系数a指的是另外一边的系数

    def __init__(self, a1, a2, N, M):
        self.a1 = a1
        self.a2 = a2
        self.N = N # 代表1-N
        self.M = M # 代表1-M
        self.Group = np.zeros([3, N, M], dtype=float)
        if (a2 * a1) >= 1:
            pass
        else:
            self.profits()

    def profits(self):
        # for i in range(1, 4):
        #     self.Group[i][0][0] = 1 - (self.a1 + self.a2)/2
        for i in range(self.N): # 从N=1开始
            for j in range(self.M): # 从M=1开始
                self.Group[0][i][j] = self.symmetric(i, self.a2) + self.symmetric(j, self.a1)
        for i in range(1, self.N): # 从N=2开始
            for j in range(1, self.M): # 从M=2开始
                asymmetric = self.asymmetric(i, j, self.a1, self.a2)
                self.Group[1][i][j] = asymmetric[0]
                self.Group[2][i][j] = asymmetric[1]

    def symmetric(self, num_1, a):
        # 计算对称歧视情况下的收入
        num = num_1 + 1 # 对应真正的分段数 
        point1 = (num - 2) / 2 # 不一定是整数
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

    def asymmetric(self, N_1, M_1, a1, a2):
        # 绘制不对称歧视情况下的利润 N>1, M>1
        N = N_1 + 1
        M = M_1 + 1
        na_1 = (M + N*a1 + N*a2 - 3*M*N - M*N*a2 + 2*M*N*(a1**2) + 3*M*N*(a2**2) + 5*M*N*a1*a2)/(4*M*N*((a1+a2)**2 - 1))
        na_2 = (N + M*a1 + M*a2 - 3*M*N - M*N*a1 + 3*M*N*(a1**2) + 2*M*N*(a2**2) + 5*M*N*a1*a2)/(4*M*N*((a1+ a2)**2 - 1))
        nb_1 = 1-na_1
        nb_2 = 1-na_2
        pb_1 = 1/2 - (a1 + 2*a2)/2 + 1/(2*N)
        pb_2 = 1/2 - (a2 + 2*a1)/2 + 1/(2*M)
        point1 = math.floor(na_1 * N - 1/2) + 2
        point2 = math.floor(na_2 * M - 1/2) + 2
        v1 = 0
        v2 = 0
        for i in range(1, point1+1):
            if i <= point1-2:
                temp = (a1*(na_2 - nb_2) - 2*i/N + pb_1 + 1) / N
                v1 += temp
            else:
                xi = i/(2*N) + na_1/2 + 3/(4*N) - 1/N
                temp = (a1*(na_2 - nb_2) - 2*xi + pb_1 + 1)*(xi - (i-1)/N)
                v1 += temp
        for j in range(1, point2+1):
            if j <= point2 - 2:
                temp = (a2*(na_1 - nb_1) - 2*j/M + pb_2 + 1) / M
                v2 += temp
            else:
                yj = j/(2*M) + na_2/2 + 3/(4*M) - 1/M
                temp = (a2*(na_1 - nb_1) - 2*yj + pb_2 + 1)*(yj - (j - 1)/M)
                v2 += temp
        group = [v1+v2, pb_1*nb_1 + pb_2*nb_2]
        return group
