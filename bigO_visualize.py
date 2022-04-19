# To help understand asymptotic analysis, visualualize different functions

import math
import matplotlib.pyplot as plt

# Set up different function types
x = list(range(1, 1000))
linear = [i for i in x]
quadratic = [i**2 for i in x]
exponential = [2**i for i in x]
log2 = [math.log2(i) for i in x]
super_linear = [i * math.log(i) for i in x]

a = [math.sqrt(i) for i in x]
b = [10**i for i in x]
c = [i**1.5 for i in x]
d = [2**(math.sqrt(math.log(i))) for i in x]
e = [i**(5/3) for i in x]

# Visualize
fig, ax = plt.subplots()
ax.plot(
	#x, linear, '--',
	x, d, 'b',
	x, a, 'r',
	#x, b, 'g',
	#x, c, 'y',
	#x, e, 'p',
	#x, log2, 'g--',
	#x, super_linear, 'r',
	#x, quadratic, 'y',
	#x, exponential, 'r'
	)

# Format plot
plt.legend([
	#'Linear',
	'(d) 2^sqrt(log(x))',
	'(a) sqrt(x)',
	#'(b) 10^x',
	#'(c) x^1.5',
	#'(e) x^(5/3)',
	#'Logarithmic',
	#'Super-Linear (Linear * Log)'
	#'Quadratic',
	#'Exponential'
	])
plt.title('Plotting Different Function Growth Types')

plt.show()
