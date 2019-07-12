import cvxpy as cp
import numpy as np


def A_profit(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, i):
    # 计算给定B价格时，A的最优定价
    # B_price1, B_price2均用ndarray的形式表示
    if N != len(B_price1) or M != len(B_price2):
        print('error!')
    else:
        B_sum_price1 = np.sum(B_price1)
        B_sum_price2 = np.sum(B_price2)
        A_sum_price1 = np.sum(A_price1) - A_price1[i - 1]
        A_sum_price2 = np.sum(A_price2)
        operater = N * M * alpha1 * alpha2 - 1
        group1_stage = np.arange(N) / N
        group2_stage = np.arange(M) / M
        unit_vector1 = np.ones(N)
        unit_vector2 = np.ones(M)
        eye1 = np.eye(N)  # 单位矩阵
        eye2 = np.eye(M)
        # 定义变量A_price1,A_price2
        A_price1_i = cp.Variable()
        # 定义目标函数
        obj = cp.Maximize(
            0.5 * A_price1_i
            + alpha1 * (A_sum_price1 + A_price1_i) *
            (alpha2 * M * (A_sum_price1 + A_price1_i - B_sum_price1)) / (2 * operater)
            - 0.5 * (A_price1_i**2) + 0.5 * B_price1[i - 1] * A_price1_i
            - A_price1_i * (i - 1) / N
            + alpha2 * A_sum_price2 *
            (A_sum_price1 + A_price1_i - B_sum_price1) / (2 * operater)
        )
        # 定义约束条件
        constraints = [
            A_price1_i >= 0,
            0.5 + alpha1 * (alpha2 * M * (A_sum_price1 + A_price1_i - B_sum_price1) +
                            A_sum_price2 - B_sum_price2) / (2 * operater) -
            0.5 * (A_price1_i - B_price1[i - 1]) - i / N <= 0,
            0.5 + alpha1 * (alpha2 * M * (A_sum_price1 + A_price1_i - B_sum_price1) +
                            A_sum_price2 - B_sum_price2) / (2 * operater) -
            0.5 * (A_price1_i - B_price1[i - 1]) - (i - 1) / N >= 0
        ]
        # 求解
        prob = cp.Problem(obj, constraints)
        prob.solve()
        # status 的值：
        # OPTIMAL: 问题被成功解决
        # INFEASIBLE：问题无解
        # UNBOUNDED：无边界
        # OPTIMAL_INACCURATE：解不精确
        print('status: ', prob.status)
        print('Max value = ', prob.value)
        print(A_price1_i.value)

N = 5
M = 5
A_price1 = np.zeros(N)
A_price2 = np.zeros(M)
B_price1 = np.zeros(N)
B_price2 = np.zeros(M)
a1 = 0.01
a2 = 2
A_profit(N, M, a1, a2, A_price1, A_price2, B_price1, B_price2, N)
