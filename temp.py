import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 23,
         }

NM = np.arange(1, 11)
profit = [0.4899322175, 0.39817792453875966, 0.469256256094979, 0.5131004117650224, 0.5695896279880446,
          0.5877135899733421, 0.6168219934949997, 0.6278313269791992, 0.6445080995095251, 0.6519128975388344]
result = np.array(profit)
plt.plot(NM, result)  # 双方都歧视定价时的利润
plt.xlabel('NM', fontsize=12)
plt.ylabel(u'利润', fontsize=12)
pylab.show()
