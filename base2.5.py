import numpy as np


def nm(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2):
    A_n1 = np.empty(N)
    A_n1.fill(1 / (2 * N))
    A_n2 = np.empty(M)
    A_n2.fill(1 / (2 * M))
    B_n2 = np.empty(M)
    B_n2.fill(1 / (2 * M))
    flag = np.arange(1)
    while flag[0] < N + M:
        flag[0] = 0
        for i in range(N):
            xi = 0.5 + 0.5 * (alpha1 * (np.sum(A_n2) - np.sum(B_n2)) -
                              A_price1[i] + B_price1[i])
            if xi < i / N:
                xi = i / N
            elif xi > (i + 1) / N:
                xi = (i + 1) / N
            if A_n1[i] == xi - i / N:
                flag[0] += 1
            else:
                A_n1[i] = xi - i / N
        for j in range(M):
            Ayj = alpha2 * np.sum(A_n1) - A_price2[j]
            Byj = 1 + B_price2[j] - alpha2 * (1 - np.sum(A_n1))
            if Ayj < Byj:
                Ayj = (Ayj + Byj) / 2
                Byj = Ayj
            if Ayj < j / M:
                Ayj = j / M
            elif Ayj > (j + 1) / M:
                Ayj = (j + 1) / M
            if Byj < j / M:
                Byj = j / M
            elif Byj > (j + 1) / M:
                Byj = (j + 1) / M
            if A_n2[j] == Ayj - j / M and B_n2[j] == (j + 1) / M - Byj:
                flag[0] += 1
            else:
                A_n2[j] = Ayj - j / M
                B_n2[j] = (j + 1) / M - Byj
    result = np.concatenate((A_n1, A_n2, B_n2))
    return result


def A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    # i从零开始
    step = 1e-2
    A_price1_changed = A_price1.copy()
    A_price2_changed = A_price2.copy()
    if kind == 1:
        A_price1_changed[k] = 0
    else:
        A_price2_changed[k] = 0
    ABnm = nm(N, M, alpha1, alpha2, A_price1_changed,
              A_price2_changed, B_price1, B_price2)
    A_n1 = ABnm[0:N]
    A_n2 = ABnm[N:N + M]
    profit0 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
    if kind == 1:
        if A_n1[k] <= 0:
            return 0
        else:
            while A_n1[k] > 0:
                A_price1_changed[k] += step
                ABnm = nm(N, M, alpha1, alpha2, A_price1_changed,
                          A_price2_changed, B_price1, B_price2)
                A_n1 = ABnm[0:N]
                A_n2 = ABnm[N:N + M]
                profit1 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
                if profit0 > profit1:
                    A_price1_changed[k] -= step
                    break
                else:
                    profit0 = profit1
            return A_price1_changed[k]  # 小数点后三位
    else:
        if A_n2[k] <= 0:
            return 0
        else:
            while A_n2[k] > 0:
                A_price2_changed[k] += step
                ABnm = nm(N, M, alpha1, alpha2, A_price1_changed,
                          A_price2_changed, B_price1, B_price2)
                A_n1 = ABnm[0:N]
                A_n2 = ABnm[N:N + M]
                profit1 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
                if profit0 > profit1:
                    A_price2_changed[k] -= step
                    break
                else:
                    profit0 = profit1
            return A_price2_changed[k]  # 小数点后三位


def B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    # i从零开始
    step = 1e-2
    B_price1_changed = B_price1.copy()
    B_price2_changed = B_price2.copy()
    if kind == 1:
        B_price1_changed[k] = 0
    else:
        B_price2_changed[k] = 0
    ABnm = nm(N, M, alpha1, alpha2, A_price1,
              A_price2, B_price1_changed, B_price2_changed)
    B_n1 = 1 / N - ABnm[0:N].copy()
    B_n2 = ABnm[N + M:N + 2 * M]
    profit0 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
    if kind == 1:
        if B_n1[k] <= 0:
            return 0
        else:
            while B_n1[k] > 0:
                B_price1_changed[k] += step
                ABnm = nm(N, M, alpha1, alpha2, A_price1,
                          A_price2, B_price1_changed, B_price2_changed)
                B_n1 = 1 / N - ABnm[0:N].copy()
                B_n2 = ABnm[N + M:N + 2 * M]
                profit1 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
                if profit0 > profit1:
                    B_price1_changed[k] -= step
                    break
                else:
                    profit0 = profit1
            return B_price1_changed[k]  # 小数点后三位
    else:
        if B_n2[k] <= 0:
            return 0
        else:
            while B_n2[k] > 0:
                B_price2_changed[k] += step
                ABnm = nm(N, M, alpha1, alpha2, A_price1,
                          A_price2, B_price1_changed, B_price2_changed)
                B_n1 = 1 / N - ABnm[0:N].copy()
                B_n2 = ABnm[N + M:N + 2 * M]
                profit1 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
                if profit0 > profit1:
                    B_price2_changed[k] -= step
                    break
                else:
                    profit0 = profit1
            return B_price2_changed[k]  # 小数点后三位

N = 8
M = 8
# A_price1_temp = [0.94, 0.86, 0.78, 0.69, 0.61, 0.54, 0.46, 0.38, 0.31, 0.23, 0.13,
#                 0.07, 0.06, 0.04, 0.04, 0.04, 0.03, 0.03, 0.04, 0.03, 0.03, 0.04, 0.03, 0.03]
# A_price2_temp = [4.98, 0.83, 0.79, 0.75, 0.71, 0.66, 0.62, 0.58, 0.54, 0.5, 0.46, 1.69,
#                 1.67, 0.12, 0.09, 0.04, 0.01, 0.,   0.,   0.,   0.,   0.,   0.,   0.]
# B_price1_temp = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.03, 0.03, 0.04, 0.04, 0.03,
#                 0.05, 0.08, 0.14, 0.22, 0.3,  0.37, 0.45, 0.55, 0.61, 0.7,  0.79, 0.87, 0.95]
# B_price2_temp = [4.24, 0.04, 0.07, 0.07, 0.1,  0.12, 0.19, 0.24, 0.31, 0.36, 0.41,
# 1.88, 1.98, 0.71, 0.75, 0.79, 0.83, 0.88, 0.92, 0.96, 1.01, 1.09, 1.17,
# 1.26]
A_price1 = np.ones(N)
A_price2 = np.ones(M)
B_price1 = np.ones(N)
B_price2 = np.ones(M)
alpha1 = 0.01
alpha2 = 2
iteration = 100  # 迭代次数
for flag in range(iteration):
    for i in range(N):
        A_price1[i] = A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                 B_price1, B_price2, i, 1)
        B_price1[i] = B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                 B_price1, B_price2, i, 1)
    for j in range(M):
        A_price2[j] = A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                 B_price1, B_price2, j, 2)
        B_price2[j] = B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                 B_price1, B_price2, j, 2)
    ABnm = nm(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2)
    print(A_price1, A_price2, B_price1, B_price2, round(np.sum(
        ABnm[0:N]), 3), round(np.sum(ABnm[N:N + M]), 3), round(np.sum(ABnm[N + M:N + 2 * M]), 3))

"""
[0.94 0.86 0.78 0.69 0.61 0.53 0.46 0.38 0.31 0.23 0.13 0.07 0.06 0.04
 0.04 0.04 0.03 0.03 0.04 0.03 0.03 0.04 0.03 0.03] [4.99 0.83 0.79 0.75 0.71 0.66 0.62 0.58 0.54 0.5  0.46 1.69 1.67 0.13
 0.09 0.04 0.01 0.   0.   0.   0.   0.   0.   0.  ] [0.01 0.01 0.01 0.01 0.01 0.01 0.02 0.02 0.04 0.04 0.03 0.05 0.08 0.14
 0.22 0.31 0.37 0.45 0.55 0.61 0.7  0.79 0.87 0.95] [4.25 0.04 0.07 0.07 0.1  0.12 0.19 0.24 0.31 0.36 0.41 1.88 1.98 0.71
 0.75 0.79 0.83 0.88 0.92 0.96 1.01 1.09 1.17 1.26] 0.551 1.0 0.036
"""
