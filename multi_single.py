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
    return -(2*(alpha1**6) + 25*(alpha1**5)*alpha2 + 5*(alpha1**5) + 106*(alpha1**4)*(alpha2**2) + 
        47*(alpha1**4)*alpha2 - 45*(alpha1**4) + 188*(alpha1**3)*(alpha2**3) + 124*(alpha1**3)*(alpha2**2) - 
        370*(alpha1**3)*alpha2 - 66*(alpha1**3) + 136*(alpha1**2)*(alpha2**4) + 96*(alpha1**2)*(alpha2**3) - 
        852*(alpha1**2)*(alpha2**2) - 314*(alpha1**2)*alpha2 + 328*(alpha1**2) + 43*alpha1*(alpha2**5) + 
        15*alpha1*(alpha2**4) - 462*alpha1*(alpha2**3) - 182*alpha1*(alpha2**2) + 1360*alpha1*alpha2 + 
        216*alpha1 + 4*(alpha2**6) + (alpha2**5) - 71*(alpha2**4) - 14*(alpha2**3) + 400*(alpha2**2) + 
        72*alpha2 - 792)/(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)**2

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

# alternative setup with A turn to D and B U, temp = pi_A - pi_A0
def pi_delta1(alpha1, alpha2):
    return (((alpha1 + 3*alpha2 - 4)**2)*(alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8))/(128*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4))

# alternative setup with A turn to U and B D, temp = pi_A - pi_A0
def pi_delta2(alpha1, alpha2):
    return -(((alpha1 + 3*alpha2 - 4)**2)*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4))/(18*(alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8))

# alternative setup with APD to PD, temp = pi_B - pi_B0
def pi_delta3(alpha1, alpha2):
    return ((alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8)*(- 2*(alpha1**3) - 11*(alpha1**2)*alpha2 + 8*(alpha1**2) - 17*alpha1*(alpha2**2) + 20*alpha1*alpha2 + 9*alpha1 - 6*(alpha2**3) + 8*(alpha2**2) + 27*alpha2 - 36)**2)/(8*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4)*(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)**2)

# alternative setup with APD to NE, temp = pi_A - pi_A0
def pi_delta4(alpha1, alpha2):
    return -(2*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4)*(- alpha1**3 - 7*(alpha1**2)*alpha2 + 4*(alpha1**2) - 13*alpha1*(alpha2**2) + 16*alpha1*alpha2 + 6*alpha1 - 3*(alpha2**3) + 4*(alpha2**2) + 18*alpha2 - 24)**2)/((alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8)*(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)**2)

################### passive platforms
# alternative setup with A turn to D and B U, temp = pi_B - pi_B0
def pi_delta5(alpha1, alpha2):
    return -(((alpha1 - alpha2)**3)*(alpha1 + 3*alpha2 - 4))/(64*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4))

# alternative setup with A turn to U and B D, temp = pi_B - pi_B0
def pi_delta6(alpha1, alpha2):
    return -(- alpha1**4 + (alpha1**3)*alpha2 + 5*(alpha1**3) + 17*(alpha1**2)*(alpha2**2) - 23*(alpha1**2)*alpha2 - 6*(alpha1**2) + 15*alpha1*(alpha2**3) - 49*alpha1*(alpha2**2) + 28*alpha1*alpha2 + 16*alpha1 + 3*(alpha2**3) - 22*(alpha2**2) + 48*alpha2 - 32)/(18*(alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8))

# alternative setup with APD to PD, temp = pi_A - pi_A0
def pi_delta7(alpha1, alpha2):
    return (((alpha1 - alpha2)**2)*(- 6*(alpha1**6) - 55*(alpha1**5)*alpha2 + 34*(alpha1**5) - 188*(alpha1**4)*(alpha2**2) + 231*(alpha1**4)*alpha2 + 17*(alpha1**4) - 297*(alpha1**3)*(alpha2**3) + 557*(alpha1**3)*(alpha2**2) + 151*(alpha1**3)*alpha2 - 321*(alpha1**3) - 224*(alpha1**2)*(alpha2**4) + 587*(alpha1**2)*(alpha2**3) + 363*(alpha1**2)*(alpha2**2) - 1293*(alpha1**2)*alpha2 + 237*(alpha1**2) - 82*alpha1*(alpha2**5) + 273*alpha1*(alpha2**4) + 265*alpha1*(alpha2**3) - 1419*alpha1*(alpha2**2) + 498*alpha1*alpha2 + 756*alpha1 - 12*(alpha2**6) + 46*(alpha2**5) + 68*(alpha2**4) - 423*(alpha2**3) + 129*(alpha2**2) + 972*alpha2 - 864))/(4*(alpha1**2 + 2*alpha1*alpha2 + alpha2**2 - 4)*(7*(alpha1**2) + 22*alpha1*alpha2 + 7*(alpha2**2) - 36)**2)

# alternative setup with APD to NE, temp = pi_B - pi_B0
def pi_delta8(alpha1, alpha2):
    return (alpha1**8 + alpha1**7*alpha2 - alpha1**7 - 65*alpha1**6*alpha2**2 + 45*alpha1**6*alpha2 - 20*alpha1**6 - 365*alpha1**5*alpha2**3 + 445*alpha1**5*alpha2**2 - 26*alpha1**5*alpha2 - 14*alpha1**5 - 765*alpha1**4*alpha2**4 + 1391*alpha1**4*alpha2**3 + 454*alpha1**4*alpha2**2 - 922*alpha1**4*alpha2 + 172*alpha1**4 - 697*alpha1**3*alpha2**5 + 1721*alpha1**3*alpha2**4 + 1484*alpha1**3*alpha2**3 - 4476*alpha1**3*alpha2**2 + 680*alpha1**3*alpha2 + 312*alpha1**3 - 311*alpha1**2*alpha2**6 + 779*alpha1**2*alpha2**5 + 1784*alpha1**2*alpha2**4 - 5860*alpha1**2*alpha2**3 + 1008*alpha1**2*alpha2**2 + 4632*alpha1**2*alpha2 - 912*alpha1**2 - 91*alpha1*alpha2**7 + 203*alpha1*alpha2**6 + 782*alpha1*alpha2**5 - 2198*alpha1*alpha2**4 - 1288*alpha1*alpha2**3 + 7080*alpha1*alpha2**2 - 3936*alpha1*alpha2 - 1152*alpha1 - 12*alpha2**8 + 25*alpha2**7 + 150*alpha2**6 - 354*alpha2**5 - 572*alpha2**4 + 1800*alpha2**3 + 240*alpha2**2 - 3456*alpha2 + 2304)/((alpha1**2 + 6*alpha1*alpha2 + alpha2**2 - 8)*(7*alpha1**2 + 22*alpha1*alpha2 + 7*alpha2**2 - 36)**2)

flag = 1
if flag == 1:
    alpha1 = np.linspace(0, 4.1, 2000)
    alpha2 = np.linspace(0, 1.1, 2000)
    # 构造网格
    alpha1, alpha2 = np.meshgrid(alpha1,alpha2)
    pi_A_1 = pi_A_1(alpha1, alpha2)
    pi_A_2 = pi_A_2(alpha1, alpha2)
    pi_A_3 = pi_A_3(alpha1, alpha2)
    # pi_delta1 = pi_delta1(alpha1, alpha2)
    # pi_delta2 = pi_delta2(alpha1, alpha2)
    # pi_delta3 = pi_delta3(alpha1, alpha2)
    # pi_delta4 = pi_delta4(alpha1, alpha2)
    # pi_delta5 = pi_delta5(alpha1, alpha2)
    # pi_delta6 = pi_delta6(alpha1, alpha2)
    # pi_delta7 = pi_delta7(alpha1, alpha2)
    # pi_delta8 = pi_delta8(alpha1, alpha2)
    pi_A_4 = pi_A_4(alpha1, alpha2)
    pi_B_4 = pi_B_4(alpha1, alpha2)
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
    plt.contour(alpha1, alpha2, alpha1*alpha2 - 1, 0, colors='black')
    plt.contour(alpha1, alpha2, alpha1+ 3*alpha2 - 4, 0, colors='black')
    # plt.contour(alpha1, alpha2, alpha1+ alpha2 - 2, 0, colors='black')
    plt.contour(alpha1, alpha2, pi_A_4 - pi_A_1, 0, colors='red')
    # plt.contour(alpha1, alpha2, alpha1 - 4, 0, colors='black')
    # plt.contour(alpha1, alpha2, alpha1 - 1, 0, colors='black')
    plt.contour(alpha1, alpha2, pi_A_3, 0, colors='blue')
    # plt.contour(alpha1, alpha2, (-1/2 - alpha1*alpha2/4)-pi_A_2, 0, colors='blue')

    # plt.contour(alpha1, alpha2, pi_delta2 - 0.1, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_delta1, 0, colors='black')
    # plt.contour(alpha1, alpha2, pi_delta3, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_delta4 - 0.2, 0, colors='grey')
    # plt.contour(alpha1, alpha2, pi_delta5, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_delta6 - 1, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_delta7, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_delta8, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_A_3 , 0, colors='blue')
    # plt.contour(alpha1, alpha2, pi_A_4 - pi_B_4, 0, colors='red')
    # plt.contour(alpha1, alpha2, pi_A_4 - pi_A_1, 0, colors='green')
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
    alpha1 = 1.4
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
    # print(pi_A_3-pi_A_2)
    print(na_1+nb_1-1)
    # print(nb_2)
    # print(SW1 - (alpha1 + alpha2 - 5/4))
    # print(pi_B_4 - pi_A_1)
    # print(SW4 - SW3)