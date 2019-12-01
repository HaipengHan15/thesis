import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

flag = 1
if flag == 1:
    alpha1 = np.linspace(0, 2.5, 1000)
    alpha2 = np.linspace(0, 2.5, 1000)
    # 构造网格
    alpha1, alpha2 = np.meshgrid(alpha1,alpha2)
else:
    alpha1 = 0
    alpha2 = 1.99
z1 = alpha1*alpha2 # 交叉网络外部性大小
# n^A_1, n^B_1
z2 = (alpha1*alpha2 - 1)*2/(alpha1**2 + alpha2**2 +4*alpha1*alpha2 - 6)
# n^A_2, n^B_2
z3 = (alpha1*alpha2 - 1)*(alpha1 + alpha2)/(alpha1**2 + alpha2**2 +4*alpha1*alpha2 - 6)
pi_A_1 = -((alpha1**5)*alpha2 + 5*(alpha1**4)*(alpha2**2) - (alpha1**4) + 8*(alpha1**3)*(alpha2**3) -
           14*(alpha1**3)*alpha2 + 5*(alpha1**2)*(alpha2**4) - 30*(alpha1**2)*(alpha2**2) +
           9*(alpha1**2) + alpha1*(alpha2**5) - 14*alpha1*(alpha2**3) + 42*alpha1*alpha2 -
           (alpha2**4) + 9*(alpha2**2) - 20)/((alpha1**2) + 4*alpha1*alpha2 + (alpha2**2) - 6)**2
# pi_A_2 = - (alpha1**2)/16 - (3*alpha1*alpha2)/8 - (alpha2**2)/16 + 1/2
pi_A_2 = - (alpha1+alpha2)/2 + 1
z5 = pi_A_1 - pi_A_2
# 绘制等高线
# plt.contour(alpha1, alpha2, z1-1, 0, colors='black')
plt.contour(alpha1, alpha2, z2-1, 0, colors='black')
# plt.contour(alpha1, alpha2, z2-1/2, 0, colors='blue')
# plt.contour(alpha1, alpha2, z3-1/2, 0, colors='yellow')
# plt.contour(alpha1, alpha2, z3-1, 0, colors='pink')
# plt.contour(alpha1, alpha2, z5, 0, colors='red')
plt.axis('scaled')
plt.show()

# print(z5)