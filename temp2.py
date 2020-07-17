from scipy import integrate
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

# def condition12(alpha1, X):
#     return X - (167 - 161*alpha1 + 21*(57**0.5)*(1-alpha1))/(2*(688 - 875*alpha1 + 196*(alpha1**2)))

# def condition23(alpha1, X):
#     return X - (175*alpha1 - 169 - 21*(57**0.5)*(1-alpha1))/(2*(856 - 2219*alpha1 + 1372*(alpha1**2)))

# def condition2(alpha1, X):
#     return X - 1/(4*alpha1  - 1)

# flag = 1
# if flag == 1:
#     alpha1 = np.linspace(0, 1.1, 1000)
#     X = np.linspace(0, 1.1, 1000)
#     # 构造网格
#     alpha1, X = np.meshgrid(alpha1,X)
#     condition12 = condition12(alpha1, X)
#     condition23 = condition23(alpha1, X)
#     condition2 = condition2(alpha1, X)
#     # SW1 = SW1(alpha1, alpha2)
#     # SW2 = SW2(alpha1, alpha2)
#     # SW3 = SW3(alpha1, alpha2)
#     # SW4 = SW4(alpha1, alpha2)
#     # 绘制等高线
#     # plt.contour(alpha1, X, alpha1 - 1, 0, colors='black')
#     # plt.contour(alpha1, X, alpha1 - 1/4, 0, colors='black')
#     plt.contour(alpha1, X, alpha1 - 4/7, 0, colors='black')
#     # plt.contour(alpha1, X, condition12, 0, colors='black')
#     plt.contour(alpha1, X, condition23, 0, colors='black')
#     # plt.contour(alpha1, X, condition2, 0, colors='black')
#     # plt.contour(alpha1, X, 856 - 2219*alpha1 + 1372*(alpha1**2), 0, colors='red')
#     plt.axis('scaled')
#     plt.show()
def condition12(alpha1):
    return (167 - 161*alpha1 + 21*(57**0.5)*(1-alpha1))/(2*(688 - 875*alpha1 + 196*(alpha1**2)))
def condition23(alpha1):
    return (175*alpha1 - 169 - 21*(57**0.5)*(1-alpha1))/(2*(856 - 2219*alpha1 + 1372*(alpha1**2)))
def condition2(alpha1):
    return 1/(4*alpha1  - 1)
def condition3(alpha1):
    return 1/(7*alpha1  - 4)
def condition4(alpha1):
    return 1/(14*alpha1  - 11)
def condition5(alpha1):
    return 1/(10 - 7*alpha1)
condition12 = np.frompyfunc(condition12,1,1)
alpha1 = np.linspace(0, 1, 2000)
alpha2 = np.linspace(0.65, 1, 2000)
alpha3 = np.linspace(4.01/7, 1, 2000)
alpha4 = np.linspace(11.01/14, 1, 2000)
alpha5 = np.linspace(0, 1, 2000)
X1=condition12(alpha1)
X2=condition23(alpha2)
X3=condition3(alpha3)
X4=condition4(alpha4)
X5=condition5(alpha5)
plt.plot(alpha1, X1, c='black')
plt.plot(alpha2, X2, c='black')
plt.plot(alpha3, X3, c='black', linestyle="--")
plt.plot(alpha4, X4, c='black', linestyle="--")
plt.plot(alpha5, X5, c='black', linestyle="--")
# plt.vlines(1/4, 0, 2.1, linestyle="--")
plt.vlines((317-9*(57**0.5))/392, 0, 3, linestyle="--")
plt.vlines(1, 0, 3)
plt.hlines(1/3, 0, 1, linestyle="--")
plt.ylim(0, 3)
plt.xlim(0, 1.1)
plt.xticks([])
plt.yticks([])
plt.show()