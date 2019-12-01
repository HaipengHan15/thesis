import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
import sympy
sympy.init_printing()
from sympy import I, pi, oo

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

alpha1, alpha2 = sympy.Symbols("alpha1, alpha2", positive=True)
pi_A_1 = -((alpha1**5)*alpha2 + 5*(alpha1**4)*(alpha2**2) - (alpha1**4) + 8*(alpha1**3)*(alpha2**3) -
           14*(alpha1**3)*alpha2 + 5*(alpha1**2)*(alpha2**4) - 30*(alpha1**2)*(alpha2**2) +
           9*(alpha1**2) + alpha1*(alpha2**5) - 14*alpha1*(alpha2**3) + 42*alpha1*alpha2 -
           (alpha2**4) + 9*(alpha2**2) - 20)/((alpha1**2) + 4*alpha1*alpha2 + (alpha2**2) - 6)**2
pi_A_2 = - (alpha1**2)/16 - (3*alpha1*alpha2)/8 - (alpha2**2)/16 + 1/2

sympy.solve(alpha1**2 + alpha2**2 - 2)