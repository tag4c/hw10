import numpy as np
import matplotlib.pyplot as plt
import math

def approxpi(n):

	piapprox = 0.0
	x = np.array(np.random.random(n)) # array between 0-1 of size n
	y = np.array(np.random.random(n))
	xinside = []  # r < 1
	xoutside = [] # r >= 1
	yinside = []
	youtside = []
# find out inside or outside	
	for i in range (1, n):
		r = np.sqrt(np.square(x[i]) + np.square(y[i]))
		if r < 1:
			xinside.append(x[i])
			yinside.append(y[i])
		else:
			xoutside.append(x[i])
			youtside.append(y[i])
	
	# plot the stuff
	fname = "plot" + str(n) + ".png"
	plt.plot(xinside,yinside, '+r')
	plt.plot(xoutside,youtside, '+b')
	plt.savefig(fname)
	piapprox = 4 * ((1.0 * len(xinside)) / n)

	return piapprox
def main():
	pi1 = approxpi(100)
	pi2 = approxpi(1000)
	pi3 = approxpi(10000)
	print "At 100 points, pi is approximately: " + str(pi1)
	print "At 1000 points, pi is approximately: " + str(pi2)
	print "At 10000 points, pi is approximately: " + str(pi3)

main()
