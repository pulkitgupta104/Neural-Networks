import numpy as np

train=np.array([[1,1,1,1,-1,-1],[-1,1,1,1,1,1]])
W = np.dot(train.T,train)
for x in range (6):
	W[x][x] = 0
#print W

I = np.array([[1,1,1,0,1,0],[0,1,0,1,1,1,],[0,0,1,1,1,1]])
print I

	