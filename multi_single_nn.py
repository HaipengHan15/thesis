import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

# group-1 multi-homing, PD, Pa_2 = Pb_2 = 0
def pi_A_1(alpha1, alpha2):
    return (alpha1**2)/18 - alpha1/9 - alpha1*alpha2/2 + 5/9

# group-1 single-homing, Pa_i = Pb_i = 0 / NE, Pa_1 = Pb_1 = 0
def pi_A_2(alpha1, alpha2):
    return 1/2 - alpha1*alpha2/2

# group-1 NE, Pa_2 = Pb_2 = 0
def pi_A_3(alpha1, alpha2):
    # return alpha1**2/16
    return (alpha1**2)*(-1 + alpha1*alpha2)*(- 2 + 
                    alpha1*alpha2)/((8 - 6*alpha1*alpha2)*(4 - 3*alpha1*alpha2))

# group-1 multi-homing, APD
def Pa_11(alpha1, alpha2):
    return -(- alpha1**3 + 3*(alpha1**2)*alpha2 - 3*(alpha1**2) + 18*alpha1*(alpha2**2) - 
        18*alpha1*alpha2 + 3*alpha1 + 4*(alpha2**3) - 3*(alpha2**2) - 27*alpha2 + 
        24)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 multi-homing, APD
def Pa_12(alpha1, alpha2):
    return -(- 2*(alpha1**3) - 4*(alpha1**2)*alpha2 + (alpha1**2) + 5*alpha1*(alpha2**2) - 
        2*alpha1*alpha2 + 9*alpha1 + alpha2**3 + alpha2**2 - 9*alpha2)/(7*(alpha1**2) + 
        22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 multi-homing, APD
def Pb_1(alpha1, alpha2):
    return (alpha1**3 + 3*(alpha1**2) - 9*alpha1*(alpha2**2) + 6*alpha1*alpha2 - 
        6*alpha1 - 4*(alpha2**3) + 3*(alpha2**2) + 18*alpha2 - 12)/(7*(alpha1**2) + 
        22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 multi-homing, APD
def na_11(alpha1, alpha2):
    return ((alpha1 + alpha2)*(2*(alpha1**2) + 6*alpha1*alpha2 - 
        alpha1 + alpha2**2 + alpha2 - 9))/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 NE, Pa_2 = Pb_2 = 0
def na_1(alpha1, alpha2):
    return (alpha1*(alpha1*alpha2-2))/(2*(3*alpha1*alpha2 - 4))

# PD
def SW1(alpha1, alpha2):
    return (5*(alpha1**2) + 8*alpha1 + 6*alpha2*alpha1 - 13 + 12*alpha2)/36

def SW2(alpha1, alpha2):
    return (alpha1+alpha2)/2 - 1/2

# NE
def SW3(alpha1, alpha2):
    return (3*(alpha1**2) + 4*alpha2*alpha1 - 4)/16


flag = 1
if flag == 1:
    alpha1 = np.linspace(0, 4.5, 1000)
    alpha2 = np.linspace(0, 1.5, 1000)
    # 构造网格
    alpha1, alpha2 = np.meshgrid(alpha1,alpha2)
    pi_A_1 = pi_A_1(alpha1, alpha2)
    pi_A_2 = pi_A_2(alpha1, alpha2)
    pi_A_3 = pi_A_3(alpha1, alpha2)
    # Pa_11 = Pa_11(alpha1, alpha2)
    # Pa_12 = Pa_12(alpha1, alpha2)
    # Pb_1 = Pb_1(alpha1, alpha2)
    na_1 = na_1(alpha1, alpha2)
    # SW1 = SW1(alpha1, alpha2)
    # SW2 = SW2(alpha1, alpha2)
    # SW3 = SW3(alpha1, alpha2)
    # CS1 = (13*alpha1)/9 + (4*alpha2)/3 + (alpha1*alpha2)/6 + alpha1**2/36 - 89/36
    # CS2 = (3*alpha1)/2 + (3*alpha2)/2 - 5/2
    # CS3 = 5*(alpha1**2)/16 + (9*alpha1*alpha2)/8 + 5*(alpha2**2)/16 - 5/4
    # 绘制等高线
    plt.contour(alpha1, alpha2, alpha1*alpha2 - 1, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1 + alpha2 - 2, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1 + alpha2 - 4, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1 - 4, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1 - 1, 0, colors='black')

    plt.contour(alpha1, alpha2, pi_A_1 - pi_A_3, 0, colors='yellow')
    # plt.contour(alpha1, alpha2, pi_A_1 - pi_A_2, 0, colors='green')
    # plt.contour(alpha1, alpha2, Pa_11, 0, colors='brown')
    # plt.contour(alpha1, alpha2, Pa_12, 0, colors='grey')
    # plt.contour(alpha1, alpha2, Pb_1, 0, colors='red')
    plt.contour(alpha1, alpha2, na_1-1/2, 0, colors='blue')
    # plt.contour(alpha1, alpha2, na_11-1, 0, colors='red')
    # plt.contour(alpha1, alpha2, CS2 - CS3, 0, colors='orange')
    plt.axis('scaled')
    plt.show()
else:
    alpha1 = 2.2
    alpha2 = 0.01
    pi_A_1 = pi_A_1(alpha1, alpha2)
    pi_A_2 = pi_A_2(alpha1, alpha2)
    pi_A_3 = pi_A_3(alpha1, alpha2)
    na_11 = na_11(alpha1, alpha2)
    SW1 = SW1(alpha1, alpha2)
    SW2 = SW2(alpha1, alpha2)
    SW3 = SW3(alpha1, alpha2)
    print(na_11)
    # print(pi_B_4 - pi_A_3)
    # print(pi_A_1 - pi_A_3)
    # print(pi_B_4 - pi_A_1)
    # print(SW4 - SW3)