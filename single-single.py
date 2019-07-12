import numpy as np
from openpyxl import load_workbook
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
import base1

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }


def nm(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2):
    operator = N*M*alpha1*alpha2-1
    A_n1 = np.zeros(N)
    A_n2 = np.zeros(M)
    flag = np.arange(1)
    while flag[0] < N + M:
        flag[0] = 0
        for i in range(N):  # i从0开始
            xi = 0.5 + alpha1*0.5*(M*alpha2*(np.sum(A_price1)-np.sum(B_price1))+(
                np.sum(A_price2)-np.sum(B_price2)))/operator - 0.5*(A_price1[i]-B_price1[i])
            if xi < i / N:
                xi = i / N
            elif xi > (i + 1) / N:
                xi = (i + 1) / N
            if A_n1[i] == xi - i / N:
                flag[0] += 1
            else:
                A_n1[i] = xi - i / N
        for j in range(M):  # j从0开始
            yj = 0.5 + alpha2*0.5*(N*alpha1*(np.sum(A_price2)-np.sum(B_price2))+(
                np.sum(A_price1)-np.sum(B_price1)))/operator - 0.5*(A_price2[j]-B_price2[j])
            if yj < j / M:
                yj = j / M
            elif yj > (j + 1) / M:
                yj = (j + 1) / M
            if A_n2[j] == yj - j / M:
                flag[0] += 1
            else:
                A_n2[j] = yj - j / M
    result = np.concatenate((A_n1, A_n2, flag))
    return result


def A_profit(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2):
    ABnm_temp = nm(N, M, alpha1, alpha2, A_price1,
                   A_price2, B_price1, B_price2)
    A_n1_temp = ABnm_temp[0:N]
    A_n2_temp = ABnm_temp[N:N + M]
    profit_temp = A_price1.T @ A_n1_temp + A_price2.T @ A_n2_temp
    return profit_temp


def B_profit(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2):
    ABnm_temp = nm(N, M, alpha1, alpha2, A_price1,
                   A_price2, B_price1, B_price2)
    B_n1_temp = 1 / N - ABnm_temp[0:N].copy()
    B_n2_temp = 1 / M - ABnm_temp[N:N + M].copy()
    profit_temp = B_price1.T @ B_n1_temp + B_price2.T @ B_n2_temp
    return profit_temp


def A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    operator = N*M*alpha1*alpha2-1
    # k从零开始
    A_price1_changed = A_price1.copy()
    A_price2_changed = A_price2.copy()
    if kind == 1:
        A_price1_changed[k] = (
            0.5 + M*alpha1*alpha2 *
            (np.sum(A_price1_changed)-A_price1_changed[k])/operator
            - 0.5*M*alpha1*alpha2*np.sum(B_price1)/operator
            + 0.5*(alpha1+alpha2)*np.sum(A_price2_changed)/operator
            - 0.5*alpha1*np.sum(B_price2)/operator
            + 0.5*B_price1[k] - k/N
        )/(1 - M*alpha1*alpha2/operator)
        if A_price1_changed[k] < 0:
            return 0
        ABnm = nm(N, M, alpha1, alpha2, A_price1_changed,
                  A_price2_changed, B_price1, B_price2)
        A_n1 = ABnm[0:N]
        A_n2 = ABnm[N:N + M]
        if A_n1[k] == 1/N:
            temp = A_price1_changed[k]
            A_price1_changed[k] = (
                1 - 2/N + M*alpha1*alpha2 *
                (np.sum(A_price1_changed)-np.sum(B_price1) -
                 A_price1_changed[k]+B_price1[k])/operator
                + alpha1*(np.sum(A_price2_changed) -
                          np.sum(B_price2))/operator
            )/(1 - M*alpha1*alpha2/operator) + B_price1[k]
            if temp > A_price1_changed[k]:
                print('default1!')
        elif A_n1[k] == 0:
            print('error1!')
            '''A_price1_changed[k] = (
                                                    1 + M*alpha1*alpha2 *
                                                    (np.sum(A_price1_changed)-np.sum(B_price1) -
                                                     A_price1_changed[k]+B_price1[k])/operator
                                                    + alpha1*(np.sum(A_price2_changed) -
                                                              np.sum(B_price2))/operator
                                                )/(1 - M*alpha1*alpha2/operator) + B_price1[k]'''
        if A_price1_changed[k] < 0:
            A_price1_changed[k] = 0
            print('warning1!')
        return A_price1_changed[k]  # 小数点后三位
    else:
        A_price2_changed[k] = (
            0.5 + N*alpha1*alpha2 *
            (np.sum(A_price2_changed)-A_price2_changed[k])/operator
            - 0.5*N*alpha1*alpha2*np.sum(B_price2)/operator
            + 0.5*(alpha1+alpha2)*np.sum(A_price1_changed)/operator
            - 0.5*alpha2*np.sum(B_price1)/operator
            + 0.5*B_price2[k] - k/M
        )/(1 - N*alpha1*alpha2/operator)
        if A_price2_changed[k] < 0:
            return 0
        ABnm = nm(N, M, alpha1, alpha2, A_price1_changed,
                  A_price2_changed, B_price1, B_price2)
        A_n1 = ABnm[0:N]
        A_n2 = ABnm[N:N + M]
        if A_n2[k] == 1/M:
            temp = A_price2_changed[k]
            A_price2_changed[k] = (
                1 - 2/M + N*alpha1*alpha2 *
                (np.sum(A_price2_changed)-np.sum(B_price2) -
                 A_price2_changed[k]+B_price2[k])/operator
                + alpha2*(np.sum(A_price1_changed) -
                          np.sum(B_price1))/operator
            )/(1 - N*alpha1*alpha2/operator) + B_price2[k]
            if temp > A_price2_changed[k]:
                print('default2!')
        elif A_n2[k] == 0:
            print('error2!')
            '''A_price2_changed[k] = (
                                                    1 + N*alpha1*alpha2 *
                                                    (np.sum(A_price2_changed)-np.sum(B_price2) -
                                                     A_price2_changed[k]+B_price2[k])/operator
                                                    + alpha2*(np.sum(A_price1_changed) -
                                                              np.sum(B_price1))/operator
                                                )/(1 - N*alpha1*alpha2/operator) + B_price2[k]'''
        if A_price2_changed[k] < 0:
            A_price2_changed[k] = 0
            print('warning2!')
        return A_price2_changed[k]  # 小数点后三位


def B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2, k, kind):
    operator = N*M*alpha1*alpha2-1
    # k从零开始
    B_price1_changed = B_price1.copy()
    B_price2_changed = B_price2.copy()
    if kind == 1:
        B_price1_changed[k] = (
            (k+1)/N + M*alpha1*alpha2 *
            (np.sum(B_price1_changed)-B_price1_changed[k])/operator
            - 0.5*M*alpha1*alpha2*np.sum(A_price1)/operator
            + 0.5*(alpha1+alpha2)*np.sum(B_price2_changed)/operator
            - 0.5*alpha1*np.sum(A_price2)/operator
            + 0.5*A_price1[k] - 0.5
        )/(1 - M*alpha1*alpha2/operator)
        if B_price1_changed[k] < 0:
            return 0
        ABnm = nm(N, M, alpha1, alpha2, A_price1,
                  A_price2, B_price1_changed, B_price2_changed)
        A_n1 = ABnm[0:N]
        A_n2 = ABnm[N:N + M]
        if A_n1[k] == 1/N:
            print('error3!')
            '''B_price1_changed[k] = A_price1[k] - (
                                                    1 - 2/N + M*alpha1*alpha2 *
                                                    (np.sum(A_price1)-np.sum(B_price1_changed) -
                                                     A_price1[k]+B_price1_changed[k])/operator
                                                    + alpha1*(np.sum(A_price2) -
                                                              np.sum(B_price2_changed))/operator
                                                )/(1 - M*alpha1*alpha2/operator)'''
        elif A_n1[k] == 0:
            temp = B_price1_changed[k]
            B_price1_changed[k] = A_price1[k] - (
                1 + M*alpha1*alpha2 *
                (np.sum(A_price1)-np.sum(B_price1_changed) -
                 A_price1[k]+B_price1_changed[k])/operator
                + alpha1*(np.sum(A_price2) -
                          np.sum(B_price2_changed))/operator
            )/(1 - M*alpha1*alpha2/operator)
            if temp > B_price1_changed[k]:
                print('default3!')
        if B_price1_changed[k] < 0:
            B_price1_changed[k] = 0
            print('warning3!')
        return B_price1_changed[k]  # 小数点后三位
    else:
        B_price2_changed[k] = (
            (k+1)/M + N*alpha1*alpha2 *
            (np.sum(B_price2_changed)-B_price2_changed[k])/operator
            - 0.5*N*alpha1*alpha2*np.sum(A_price2)/operator
            + 0.5*(alpha1+alpha2)*np.sum(B_price1_changed)/operator
            - 0.5*alpha2*np.sum(A_price1)/operator
            + 0.5*A_price2[k] - 0.5
        )/(1 - N*alpha1*alpha2/operator)
        if B_price2_changed[k] < 0:
            return 0
        ABnm = nm(N, M, alpha1, alpha2, A_price1,
                  A_price2, B_price1_changed, B_price2_changed)
        A_n1 = ABnm[0:N]
        A_n2 = ABnm[N:N + M]
        if A_n2[k] == 1/M:
            print('error4!')
            '''B_price2_changed[k] = A_price2[k] - (
                                                    1 - 2/M + N*alpha1*alpha2 *
                                                    (np.sum(A_price2)-np.sum(B_price2_changed) -
                                                     A_price2[k]+B_price2_changed[k])/operator
                                                    + alpha2*(np.sum(A_price1) -
                                                              np.sum(B_price1_changed))/operator
                                                )/(1 - N*alpha1*alpha2/operator)'''
        elif A_n2[k] == 0:
            temp = B_price2_changed[k]
            B_price2_changed[k] = A_price2[k] - (
                1 + N*alpha1*alpha2 *
                (np.sum(A_price2)-np.sum(B_price2_changed) -
                 A_price2[k]+B_price2_changed[k])/operator
                + alpha2*(np.sum(A_price1) -
                          np.sum(B_price1_changed))/operator
            )/(1 - N*alpha1*alpha2/operator)
            if temp > B_price2_changed[k]:
                print('default4!')
        if B_price2_changed[k] < 0:
            B_price2_changed[k] = 0
            print('warning4!')
        return B_price2_changed[k]  # 小数点后三位


alpha1 = 0.1
alpha2 = 0.1
profit_NM = []
profit_1_NM = []
profit_2_NM = []
data_to_save = []
for NM in range(4, 5):
    print('N = M = ', NM)
    N = NM
    M = NM
    A_price1 = np.zeros(N)
    A_price2 = np.zeros(M)
    B_price1 = np.zeros(N)
    B_price2 = np.zeros(M)
    for a in range(50):
        A_price1_previous = A_price1.copy()
        A_price2_previous = A_price2.copy()
        for i in range(N):
            A_price1[i] = A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                     B_price1, B_price2, i, 1)
            print('1')
            B_price1[N-1-i] = B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                         B_price1, B_price2, N-1-i, 1)
            print('2', i)
        for j in range(M):
            B_price2[M-1-j] = B_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                     B_price1, B_price2, M-1-j, 2)
            print('3')
            A_price2[j] = A_profit_k(N, M, alpha1, alpha2, A_price1, A_price2,
                                         B_price1, B_price2, j, 2)
            print('4', j)
        ABnm = nm(N, M, alpha1, alpha2, A_price1, A_price2, B_price1, B_price2)
        An1 = np.sum(ABnm[0:N])
        An2 = np.sum(ABnm[N:N + M])
        print(A_price1, A_price2, B_price1, B_price2,
              round(An1, 3), round(An2, 3))
        if (abs(A_price1_previous - A_price1) < (1e-2) / N).all() and \
                (abs(A_price2_previous - A_price2) < (1e-2) / M).all() and \
                abs(An1 - 0.5) < (1e-2) and abs(An2 - 0.5) < (1e-2):
            profit_1 = A_price1.T @ ABnm[0:N]
            profit_2 = A_price2.T @ ABnm[N:N + M]
            profit = profit_1 + profit_2
            profit_1_NM.append(profit_1)
            profit_2_NM.append(profit_2)
            profit_NM.append(profit)
            data_to_save.append(ABnm[0:N].tolist())
            data_to_save.append(ABnm[N:N + M].tolist())
            break
'''
print(data_to_save)
print(profit_NM)
NM = np.arange(1, 8)
result = np.array(profit_NM)
result_1 = np.array(profit_1_NM)
result_2 = np.array(profit_2_NM)
# plt.plot(NM, result)  # 双方都歧视定价时的利润
plt.plot(NM, result_1)
# plt.plot(NM, result_2)
N = np.arange(1, 8)
M = np.arange(1, 8)
base = base1.base1(0.1, 0.08, N, M)
group1_result = base.Group1[1]
plt.plot(N, group1_result)  # 双方都歧视定价时的利润
plt.xlabel('NM', fontsize=12)
plt.ylabel(u'利润', fontsize=12)
pylab.show()
'''

""" NM=11
[8.17067467e-01 6.35249285e-01 4.53562478e-01 2.71744296e-01
 9.32884993e-02 3.50333938e-04 0.00000000e+00 0.00000000e+00
 0.00000000e+00 0.00000000e+00 0.00000000e+00] [0.90692556 0.81601646 0.72510737 0.63419828 0.54328919 0.4523801
 0.36124247 0.27033338 0.17942429 0.08881079 0.00471856] [0.00000000e+00 0.00000000e+00 0.00000000e+00 0.00000000e+00
 3.50333938e-04 3.50333938e-04 8.99261145e-02 2.71744296e-01
 4.53562478e-01 6.35380660e-01 8.17198842e-01] [0.00205821 0.09240172 0.18367209 0.27388051 0.3647896  0.45569869
 0.54660779 0.63751688 0.72842597 0.82003573 0.91094482] 0.499 0.993 1.0
"""
