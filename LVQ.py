import numpy as np

I = np.array([[1,1,1,-1],[-1,-1,-1,1],[1,-1,-1,-1],[-1,-1,1,1],[-1,1,1,1],[-1,1,-1,-1]])
T = np.array([1,2,2,1,1,2])
W = np.array([[1.0,-1],[1,-1],[1,-1],[-1,1]])

r = 0.9

for x in range(1000):
	for y in range(6):
		k1 = k2 = 0
		
		for z in range(4):
			k1 = k1 + (W[z][0] - I[y][z])**2
			k2 = k2 + (W[z][1] - I[y][z])**2

		# print ("y , k1 ,k2 ")
		# print (y,k1,k2)

		if(k1 == k2):
			if(T[y] == 2):
				for z in range(4):
					W[z][0] = W[z][0] - r * (I[y][z] - W[z][0])
					W[z][1] = W[z][1] + r * (I[y][z] - W[z][1])

			elif(T[y] == 1):
				for z in range(4):
					W[z][0] = W[z][0] + r * (I[y][z] - W[z][0])
					W[z][1] = W[z][1] - r * (I[y][z] - W[z][1])
			continue	

		min = 0 if (k1 < k2) else 1
		if(min == T[y] - 1):
			for z in range(4):
				W[z][min] = W[z][min] + r * (I[y][z] - W[z][min])
		else:
			for z in range(4):
				W[z][min] = W[z][min] - r * (I[y][z] - W[z][min])

	r = r * 0.5
print W , r
print ("\n")