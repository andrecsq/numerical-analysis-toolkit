import numpy as np

def check_symmetric(A, rtol=1e-05, atol=1e-08):
    is_symmetric = np.allclose(A, A.T, rtol=rtol, atol=atol)

    if (not is_symmetric):
        print("A is not symmetric")
        quit()

# A deve ser simétrica

A = np.array([[6, 2, 1, -2],
              [2, 8, -1, -1],
              [1, -1, 5, 1],
              [-2, -1, 1, 6]])

check_symmetric(A)

print("A: ")
print(A)

n = A.shape[0]

print(f"n = {n}")
print()

D = np.zeros((n,n))
D[0,0]=A[0,0]
L = np.identity(n)

for i in range(n):
	s = 0
	for k in range(i):
		s += float(L[i,k]*L[i,k]*D[k,k])
	D[i,i] = A[i,i] - s
	print(f"D[{i}] = A[{i},{i}]({A[i,i]}) - s({s})")

	for j in range(i+1, n):
		s = 0
		for k in range(i):
			s += float(L[j,k]*L[i,k]*D[k,k])
		L[j,i] = (A[j,i]-s)/D[i,i]
		print(f"L[{j},{i}] = (A[{j},{i}]({A[j,i]}) - s({s}))/D[{i}] = {L[j,i]}")
		print()

print("L =")
print(L)

print(f"D =")
print(D)