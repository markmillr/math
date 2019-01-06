# gibbs.py

# demonstrates the Gibbs phenomenen, that the oscillations of the partial sums of Fourier series
# do not (necessarily?) decrease as they approach a jump discontinuity

import numpy as np
import matplotlib.pyplot as plt

x_ = np.linspace(-1, 1, num=1000)
Nx = 10  # number of points to consider
Nh = 100  # number of harmonics
T = 8

def testfunction(x):
	result = None
	if x >= -1 and x <= 0:
		print(x)
		result = -1.
	elif x > 0 and x <= 1:
		result = 1.
	return result

def wn(n):
	global T
	wn = (2*np.pi*n)/T
	return wn

def bn(n):
	n = int(n)
	if (n%2 != 0):
		return 4/(np.pi*n)
	else:
		return 0


def fourierSeries(x, n_max=None):
	a0 = 0.
	partialSums = 0.
	for n in range(1,n_max):
		try:
			partialSums = partialSums + bn(n)*np.sin(wn(n)*x)
		except:
			print("nahh")
			pass
	return partialSums




x = []
y = []
f = []

for i in x_:
	#print(testfunction(i))
	x.append(i)
	y.append(testfunction(i))

	f.append(fourierSeries( i, n_max=Nh))

for i in range(0, len(y)):
	print(x[i], y[i])

fig, ax = plt.subplots()
plt.style.use("ggplot")
ax.plot(x_,y, color="purple", label="Signal")
ax.plot(x_,f, color="green", label="Fourier")
plt.legend()
ax.set_title("Fourier series approximation: Nh = {}".format(Nh))
plt.show()


