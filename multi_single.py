import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

# group-1 multi-homing, PD
def pi_A_1(alpha1, alpha2):
    return (alpha1**2)/18 - (11*alpha1)/18 - alpha2/2 + 19/18

# group-1 single-homing
def pi_A_2(alpha1, alpha2):
    return - (alpha1+alpha2)/2 + 1

# group-1 multi-homing, NE
def pi_A_3(alpha1, alpha2):
    return - (alpha1**2)/16 - (3*alpha1*alpha2)/8 - (alpha2**2)/16 + 1/2

# group-1 APD
def pi_A_4(alpha1, alpha2):
    return -(- alpha1**6 - 2*alpha1**5*alpha2 + 22*alpha1**5 + 15*alpha1**4*alpha2**2 + 
        162*alpha1**4*alpha2 - 37*alpha1**4 + 44*alpha1**3*alpha2**3 + 398*alpha1**3*alpha2**2 - 
        308*alpha1**3*alpha2 - 226*alpha1**3 + 22*alpha1**2*alpha2**4 + 382*alpha1**2*alpha2**3 - 
        672*alpha1**2*alpha2**2 - 938*alpha1**2*alpha2 + 457*alpha1**2 - 4*alpha1*alpha2**5 + 
        164*alpha1*alpha2**4 - 320*alpha1*alpha2**3 - 902*alpha1*alpha2**2 + 1606*alpha1*alpha2 + 
        576*alpha1 - 2*alpha2**6 + 24*alpha2**5 - 31*alpha2**4 - 238*alpha2**3 + 
        457*alpha2**2 + 576*alpha2 - 1224)/(7*alpha1**2 + 22*alpha1*alpha2 + 7*alpha2**2 - 36)**2

# group-1 APD
def pi_B_4(alpha1, alpha2):
    return -(2*alpha1**6 + 25*alpha1**5*alpha2 + 5*alpha1**5 + 106*alpha1**4*alpha2**2 + 
        47*alpha1**4*alpha2 - 45*alpha1**4 + 188*alpha1**3*alpha2**3 + 124*alpha1**3*alpha2**2 - 
        370*alpha1**3*alpha2 - 66*alpha1**3 + 136*alpha1**2*alpha2**4 + 96*alpha1**2*alpha2**3 - 
        852*alpha1**2*alpha2**2 - 314*alpha1**2*alpha2 + 328*alpha1**2 + 43*alpha1*alpha2**5 + 
        15*alpha1*alpha2**4 - 462*alpha1*alpha2**3 - 182*alpha1*alpha2**2 + 1360*alpha1*alpha2 + 
        216*alpha1 + 4*alpha2**6 + alpha2**5 - 71*alpha2**4 - 14*alpha2**3 + 400*alpha2**2 + 
        72*alpha2 - 792)/(7*alpha1**2 + 22*alpha1*alpha2 + 7*alpha2**2 - 36)**2

# group-1 APD
def na_1(alpha1, alpha2):
    return (2*(alpha1**3) + 8*(alpha1**2)*alpha2 - alpha1**2 + 7*alpha1*(alpha2**2) - 9*alpha1 + 
        alpha2**3 + alpha2**2 - 9*alpha2)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 APD
def nb_1(alpha1, alpha2):
    return (alpha1**3 + 3*(alpha1**2)*alpha2 + 3*(alpha1**2) + alpha1*(alpha2**2) + 8*alpha1*alpha2 - 
        6*alpha1 + alpha2**3 + alpha2**2 - 12)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 APD
def na_2(alpha1, alpha2):
    return (4*(alpha1**2) + 12*alpha1*alpha2 - 2*alpha1 + 2*(alpha2**2) + 2*alpha2 - 
        18)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

# group-1 APD
def nb_2(alpha1, alpha2):
    return (3*(alpha1**2) + 10*alpha1*alpha2 + 2*alpha1 + 5*(alpha2**2) - 2*alpha2 - 
        18)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)

def SW1(alpha1, alpha2):
    return (5*alpha1**2)/36 + (alpha1*alpha2)/6 + (2*alpha1)/9 + alpha2/3 - 13/36

def SW2(alpha1, alpha2):
    return (alpha1+alpha2)/2 - 1/2

def SW3(alpha1, alpha2):
    return 3*((alpha1+alpha2)**2)/16 - 1/4

def SW4(alpha1, alpha2):
    return (19*alpha1**6 + 140*alpha1**5*alpha2 + 10*alpha1**5 + 363*alpha1**4*alpha2**2 + 
        82*alpha1**4*alpha2 - 215*alpha1**4 + 412*alpha1**3*alpha2**3 + 258*alpha1**3*alpha2**2 - 
        984*alpha1**3*alpha2 - 146*alpha1**3 + 232*alpha1**2*alpha2**4 + 374*alpha1**2*alpha2**3 - 
        1304*alpha1**2*alpha2**2 - 614*alpha1**2*alpha2 + 823*alpha1**2 + 54*alpha1*alpha2**5 + 
        236*alpha1*alpha2**4 - 756*alpha1*alpha2**3 - 878*alpha1*alpha2**2 + 1510*alpha1*alpha2 + 
        408*alpha1 + 4*alpha2**6 + 48*alpha2**5 - 125*alpha2**4 - 378*alpha2**3 + 763*alpha2**2 + 
        600*alpha2 - 936)/(2*(7*alpha1**2 + 22*alpha1*alpha2 + 7*alpha2**2 - 36)**2)

def temp(alpha1, alpha2):
    return alpha2 - (-(alpha1**3)/324 - 2*(alpha1**2)/27 + 59*alpha1/108 - 38/81)


flag = 1
if flag == 1:
    alpha1 = np.linspace(0, 3, 1000)
    alpha2 = np.linspace(0, 2, 1000)
    # 构造网格
    alpha1, alpha2 = np.meshgrid(alpha1,alpha2)
    pi_A_1 = pi_A_1(alpha1, alpha2)
    pi_A_2 = pi_A_2(alpha1, alpha2)
    pi_A_3 = pi_A_3(alpha1, alpha2)
    # temp = temp(alpha1, alpha2)
    # pi_A_4 = pi_A_4(alpha1, alpha2)
    # pi_B_4 = pi_B_4(alpha1, alpha2)
    # na_1 = na_1(alpha1, alpha2)
    # nb_1 = nb_1(alpha1, alpha2)
    # na_2 = na_2(alpha1, alpha2)
    # nb_2 = nb_2(alpha1, alpha2)
    # SW1 = SW1(alpha1, alpha2)
    # SW2 = SW2(alpha1, alpha2)
    # SW3 = SW3(alpha1, alpha2)
    # SW4 = SW4(alpha1, alpha2)
    # CS1 = (13*alpha1)/9 + (4*alpha2)/3 + (alpha1*alpha2)/6 + alpha1**2/36 - 89/36
    # CS2 = (3*alpha1)/2 + (3*alpha2)/2 - 5/2
    # CS3 = 5*(alpha1**2)/16 + (9*alpha1*alpha2)/8 + 5*(alpha2**2)/16 - 5/4
    # 绘制等高线
    # plt.contour(alpha1, alpha2, alpha1*alpha2 - 1, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1+alpha2 - 2, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1/2+alpha2 - 3/2, 0, colors='black')
    # plt.contour(alpha1, alpha2, alpha1 - 4, 0, colors='black')
    # plt.contour(alpha1, alpha2, alpha1 - 1, 0, colors='black')
    # plt.contour(alpha1, alpha2, pi_A_3-pi_A_2, 0, colors='red')
    # plt.contour(alpha1, alpha2, (-1/2 - alpha1*alpha2/4)-pi_A_2, 0, colors='blue')

    # plt.contour(alpha1, alpha2, temp, 0, colors='yellow')
    # plt.contour(alpha1, alpha2, pi_A_4, 0, colors='brown')
    # plt.contour(alpha1, alpha2, pi_B_4, 0, colors='red')
    # plt.contour(alpha1, alpha2, nb_1, 0, colors='red')
    # plt.contour(alpha1, alpha2, na_1+nb_1-1, 0, colors='yellow')
    # plt.contour(alpha1, alpha2, na_2, 0, colors='blue')
    # plt.contour(alpha1, alpha2, nb_2, 0, colors='green')
    # plt.contour(alpha1, alpha2, SW4 - SW1, 0, colors='grey')
    # plt.contour(alpha1, alpha2, SW1 - (alpha1 + alpha2 - 5/4), 0, colors='red')
    # plt.contour(alpha1, alpha2, CS2 - CS3, 0, colors='orange')
    plt.axis('scaled')
    plt.show()
else:
    alpha1 = 4-2*(2**0.5)
    alpha2 = 0
    pi_A_1 = pi_A_1(alpha1, alpha2)
    pi_A_2 = pi_A_2(alpha1, alpha2)
    pi_A_3 = pi_A_3(alpha1, alpha2)
    pi_A_4 = pi_A_4(alpha1, alpha2)
    pi_B_4 = pi_B_4(alpha1, alpha2)
    na_1 = na_1(alpha1, alpha2)
    nb_1 = nb_1(alpha1, alpha2)
    na_2 = na_2(alpha1, alpha2)
    nb_2 = nb_2(alpha1, alpha2)
    SW1 = SW1(alpha1, alpha2)
    SW2 = SW2(alpha1, alpha2)
    SW3 = SW3(alpha1, alpha2)
    SW4 = SW4(alpha1, alpha2)
    print(pi_A_3-pi_A_2)
    # print(na_2)
    # print(nb_2)
    # print(SW1 - (alpha1 + alpha2 - 5/4))
    # print(pi_B_4 - pi_A_1)
    # print(SW4 - SW3)