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
    alpha1 = np.linspace(0, 4, 2000)
    alpha2 = np.linspace(0, 4, 2000)
    # 构造网格
    alpha1, alpha2 = np.meshgrid(alpha1,alpha2)
else:
    alpha1 = 0
    alpha2 = 1.99
constraint1 = alpha1 + alpha2
constraint2 = alpha1*alpha2
SW_single1 = alpha1*alpha2 - 5/4
SW_single2 = (alpha1**2 + alpha2**2 +3*alpha1*alpha2 - 3)/4
SW_multi1 = 2*alpha1 + 2*alpha2 - 2
pi_single2 = - (alpha1**2 + 6*alpha1*alpha2 + alpha2**2)/16 + 1/2
pi_multi1 = alpha1 + alpha2 - 2
pi_A_2 = - (alpha1+alpha2)/2 + 1
# 绘制等高线
plt.contour(alpha1, alpha2, constraint1-2, 0, colors='black')
plt.contour(alpha1, alpha2, constraint1-4, 0, colors='black')
plt.contour(alpha1, alpha2, constraint2-1, 0, colors='black')
# plt.contour(alpha1, alpha2, SW_single1-SW_single2, 0, colors='blue')
plt.contour(alpha1, alpha2, SW_multi1-SW_single2, 0, colors='yellow')
plt.contour(alpha1, alpha2, pi_multi1-pi_single2, 0, colors='pink')
# plt.contour(alpha1, alpha2, z5, 0, colors='red')
plt.axis('scaled')
plt.show()

# print(z5)