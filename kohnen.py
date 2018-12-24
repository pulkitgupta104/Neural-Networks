import numpy as np;

I = np.array([[1,1,1,-1],[-1,-1,-1,1],[1,-1,-1,-1],[-1,-1,1,1]])
W = np.array([[0.2,0.8],[0.6,0.4],[0.5,0.7],[0.9,0.3]])
r = 0.9

for x in range(1000):									#EPOCHS
 	for y in range(4):									#CHOOSING I/P PATTERNS
		k1 = k2 = 0

		for z in range(4):								#EACH ELEMENT OF I/P
			k1 = k1 + (W[z][0] - I[y][z])**2
			k2 = k2 + (W[z][1] - I[y][z])**2
		min = 0 if (k1<k2) else 1

		for z in range(4):
			W[z][min] = W[z][min] + r * (I[y][z] - W[z][min])
	r = r * 0.5;
print W , r

for y in range(4):
	for z in range(4):
		k1 = k1 + (W[z][0] - I[y][z])**2
		k2 = k2 + (W[z][1] - I[y][z])**2
	min = 0 if (k1<k2) else 1
	print (min+1)	