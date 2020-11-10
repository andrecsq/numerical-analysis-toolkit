import numpy as np

x = np.array([1.,2.,3.,4.,5.,6.,7.,8.,9.,10.])
y = np.array([1.3, 3.5, 4.2, 5., 7., 8.8, 10.1, 12.5, 13, 15.6])

order = 2
m = x.size

print(m)

sum_x = [0] * 2*order

for i in range(2*order):
    for j in range(m):
        sum_x[i] += x[j]**i   
print("sum_x = ", sum_x) 
        
A = np.zeros((order, order))

for i in range(order):
    for j in range(order):
        A[i,j] = sum_x[i+j]

b = [0] * order

for i in range(order):
    for j in range(m):
        b[i] += (x[j]**i)*y[j]

print("A =\n", A)
print("b =", b)

x = np.linalg.solve(A, b)

print(x)
