import numpy as np
import sympy


def A_n(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, group):
    B_sum_price1 = np.sum(B_price1)
    B_sum_price2 = np.sum(B_price2)
    A_sum_price1 = np.sum(A_price1)
    A_sum_price2 = np.sum(A_price2)
    operater = N * M * alpha1 * alpha2 - 1
    if(group == 1):
        # 用户群体1
        result = np.zeros(N)
        operater1 = alpha1 * (alpha2 * M * (A_sum_price1 - B_sum_price1)
                              + A_sum_price2 - B_sum_price2) / (2 * operater)
        for k in range(N):
            result[k] = 0.5 + operater1 - 0.5 * \
                (A_price1[k] - B_price1[k]) - k / N
            if result[k] < 0:
                result[k] = 0
            if result[k] > 1 / N:
                result[k] = 1 / N
    else:
        # 用户群体2
        result = np.zeros(M)
        operater1 = alpha2 * (alpha1 * N * (A_sum_price2 - B_sum_price2)
                              + A_sum_price1 - B_sum_price1) / (2 * operater)
        for k in range(M):
            result[k] = 0.5 * alpha2 + operater1 - A_price2[k] - k / N
            if result[k] < 0:
                result[k] = 0
            if result[k] > 1 / M:
                result[k] = 1 / M
    return result


def B_n(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, group):
    B_sum_price1 = np.sum(B_price1)
    B_sum_price2 = np.sum(B_price2)
    A_sum_price1 = np.sum(A_price1)
    A_sum_price2 = np.sum(A_price2)
    operater = N * M * alpha1 * alpha2 - 1
    if(group == 1):
        # 用户群体1
        result = np.zeros(N)
        operater1 = alpha1 * (alpha2 * M * (A_sum_price1 - B_sum_price1)
                              + A_sum_price2 - B_sum_price2) / (2 * operater)
        for k in range(N):
            result[k] = (k + 1) / N - (0.5 + operater1 -
                                       0.5 * (A_price1[k] - B_price1[k]))
            if result[k] < 0:
                result[k] = 0
            if result[k] > 1 / N:
                result[k] = 1 / N
    else:
        # 用户群体2
        result = np.zeros(M)
        operater1 = alpha2 * (alpha1 * N * (A_sum_price2 - B_sum_price2)
                              + A_sum_price1 - B_sum_price1) / (2 * operater)
        for k in range(M):
            result[k] = (k + 1) / N - (-0.5 * alpha2 +
                                       operater1 + 1 + B_price2[k])
            if result[k] < 0:
                result[k] = 0
            if result[k] > 1 / M:
                result[k] = 1 / M
    return result


def A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    # i从零开始
    step = 1e-4
    A_price1_changed = A_price1.copy()
    A_price2_changed = A_price2.copy()
    if kind == 1:
        A_price1_changed[k] = 0
    else:
        A_price2_changed[k] = 0
    A_n1 = A_n(N, M, alpha1, alpha2, A_price1_changed,
               A_price2_changed, B_price1, B_price2, 1)
    A_n2 = A_n(N, M, alpha1, alpha2, A_price1_changed,
               A_price2_changed, B_price1, B_price2, 2)
    profit0 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
    if kind == 1:
        if A_n1[k] <= 0:
            return 0
        else:
            while A_n1[k] > 0:
                A_price1_changed[k] += step
                A_n1 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                           A_price2_changed, B_price1, B_price2, 1)
                A_n2 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                           A_price2_changed, B_price1, B_price2, 2)
                profit1 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
                if profit0 > profit1:
                    break
                else:
                    profit0 = profit1
            return round(A_price1_changed[k], 3)  # 小数点后三位
    else:
        if A_n2[k] <= 0:
            return 0
        else:
            while A_n2[k] > 0:
                A_price2_changed[k] += step
                A_n1 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                           A_price2_changed, B_price1, B_price2, 1)
                A_n2 = A_n(N, M, alpha1, alpha2, A_price1_changed,
                           A_price2_changed, B_price1, B_price2, 2)
                profit1 = A_price1_changed.T @ A_n1 + A_price2_changed.T @ A_n2
                if profit0 > profit1:
                    break
                else:
                    profit0 = profit1
            return round(A_price2_changed[k], 3)  # 小数点后三位


def B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    # i从零开始
    step = 1e-3
    B_price1_changed = B_price1.copy()
    B_price2_changed = B_price2.copy()
    if kind == 1:
        B_price1_changed[k] = 0
    else:
        B_price2_changed[k] = 0
    B_n1 = B_n(N, M, alpha1, alpha2, A_price1,
               A_price2, B_price1_changed, B_price2_changed, 1)
    B_n2 = B_n(N, M, alpha1, alpha2, A_price1,
               A_price2, B_price1_changed, B_price2_changed, 2)
    profit0 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
    if kind == 1:
        if B_n1[k] <= 0:
            return 0
        else:
            while B_n1[k] > 0:
                B_price1_changed[k] += step
                B_n1 = B_n(N, M, alpha1, alpha2, A_price1,
                           A_price2, B_price1_changed, B_price2_changed, 1)
                B_n2 = B_n(N, M, alpha1, alpha2, A_price1,
                           A_price2, B_price1_changed, B_price2_changed, 2)
                profit1 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
                if profit0 > profit1:
                    break
                else:
                    profit0 = profit1
            return round(B_price1_changed[k], 3)  # 小数点后三位
    else:
        if B_n2[k] <= 0:
            return 0
        else:
            while B_n2[k] > 0:
                B_price2_changed[k] += step
                B_n1 = B_n(N, M, alpha1, alpha2, A_price1,
                           A_price2, B_price1_changed, B_price2_changed, 1)
                B_n2 = B_n(N, M, alpha1, alpha2, A_price1,
                           A_price2, B_price1_changed, B_price2_changed, 2)
                profit1 = B_price1_changed.T @ B_n1 + B_price2_changed.T @ B_n2
                if profit0 > profit1:
                    break
                else:
                    profit0 = profit1
            return round(B_price2_changed[k], 3)  # 小数点后三位

N = 5
M = 5
A_price1 = np.zeros(N)
A_price2 = np.zeros(M)
B_price1 = np.zeros(N)
B_price2 = np.zeros(M)
a1 = 0.01
a2 = 2
iteration = 50  # 迭代次数
for flag in range(iteration):
    for i in range(N):
        B_price1[i] = B_profit_k(N, M, a1, a2, A_price1, A_price2,
                                 B_price1, B_price2, i, 1)
    for i in range(N):
        A_price1[i] = A_profit_k(N, M, a1, a2, A_price1, A_price2,
                                 B_price1, B_price2, i, 1)
    for j in range(M):
        B_price2[j] = B_profit_k(N, M, a1, a2, A_price1, A_price2,
                                 B_price1, B_price2, j, 2)
    for j in range(M):
        A_price2[j] = A_profit_k(N, M, a1, a2, A_price1, A_price2,
                                 B_price1, B_price2, j, 2)
    print(A_price1, A_price2, B_price1, B_price2)
