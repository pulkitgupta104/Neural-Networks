import numpy as np

S = np.array([
				[1,1,1,1,0,1,1,1,1,1,0,1,1,0,1],
				[1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
				[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
				[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1],
				[1,1,1,1,0,1,1,1,1,1,0,1,1,1,1],
				[1,1,1,1,0,1,1,1,1,1,0,0,1,0,0]
			])
S = S*2 - 1
# print S
T = np.array([[1,1,1],[-1,-1,1],[1,-1,1],[-1,1,1],[1,1,-1],[-1,-1,-1]])

W = np.dot(S.T,T)

S_T = np.dot(S,W)
print S_T.shape

T_S =  np.dot(S_T,W.T)

for x in xrange(0,5):
	print S[x]
	print T_S[x]
	print "\n"