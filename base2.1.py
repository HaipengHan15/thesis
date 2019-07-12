import cvxpy as cp
import numpy as np


def A_profit(N, M, alpha1, alpha2, B_price1, B_price2):
    # 计算给定B价格时，A的最优定价
    # B_price1, B_price2均用ndarray的形式表示
    if N != len(B_price1) or M != len(B_price2):
        print('error!')
    else:
        B_sum_price1 = np.sum(B_price1)
        B_sum_price2 = np.sum(B_price2)
        operater = N * M * alpha1 * alpha2 - 1
        group1_stage = np.arange(N) / N
        group2_stage = np.arange(M) / M
        unit_vector1 = np.ones(N)
        unit_vector2 = np.ones(M)
        eye1 = np.eye(N)  # 单位矩阵
        eye2 = np.eye(M)
        # 定义变量A_price1, A_price2, A_demand1, A_demand2
        A_price1 = cp.Variable(N)
        A_price2 = cp.Variable(M)
        A_demand1 = cp.Variable(N)
        A_demand2 = cp.Variable(M)
        # 定义目标函数
        obj = cp.Maximize(A_price1.T @ A_demand1 + A_price2.T @ A_demand2)
        # 定义约束条件
        constraints = [
            A_price1 >= 0, A_price2 >= 0, A_demand1 >= 0, A_demand2 >= 0,
            A_demand1 <= 1 / N, A_demand2 <= 1 / M,
            alpha1 * (unit_vector2.T @ A_demand2) - A_price1 -
            M * alpha1 * alpha2 * (1 - unit_vector1.T @ A_demand1) +
            alpha1 * B_sum_price2 + alpha1 * (M - 1) / 2 + B_price1 +
            1 - 2 * A_demand1 - 2 * group1_stage == 0,
            alpha2 * (unit_vector1.T @ A_demand1) - A_price2 - A_demand2 - group2_stage == 0
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
        print('Min value = ', prob.value)
        print(A_price1.value, A_price2.value, A_demand1.value, A_demand2.value)

N = 5
M = 5
B_price1 = np.zeros(N)
B_price2 = np.zeros(M)
a1 = 0.01
a2 = 2
A_profit(N, M, a1, a2, B_price1, B_price2)
