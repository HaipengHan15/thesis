from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
import pylab
import example2

plt.plot(example2.NM, example2.result)  # 双方都歧视定价时的利润
plt.plot(example2.NM, example2.result0)  # 双方都不歧视定价时的利润
plt.plot(example2.NM, example2.result2)  # 另一方不歧视时这一方歧视的利润
plt.plot(example2.NM, example2.result2B)  # 另一方歧视时这一方不歧视的利润
plt.xlabel('NM')
plt.ylabel('profit_2')
pylab.show()