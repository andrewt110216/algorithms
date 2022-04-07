# To help understand asymptotic analysis, visualualize y = x^2 to y = log(2)x

import math
import matplotlib.pyplot as plt

x = list(range(1, 8))
y_lin = [i for i in x]
y_quad2 = [i**2 for i in x]
y_exp = [2**i for i in x]
y_log2 = [math.log2(i) for i in x]

plt.plot(x, y_lin, 'r', x, y_log2, 'g--', x, y_quad2, 'y^', x, y_exp, 'go')
plt.show()
