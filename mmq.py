import numpy as np

x = np.array([0.,1.3,1.5,2.])
y = np.array([0, .7, 1, 1.5])
w = np.array([2.,2.,2.,1.])

order = 3
m = x.size

print("quant points = ", m)

sum_x = [0] * 2*order

for i in range(2*order):
    for j in range(m):
        sum_x[i] += w[j]*(x[j]**i)
print("sum_x = ", sum_x) 
        
A = np.zeros((order, order))

for i in range(order):
    for j in range(order):
        A[i,j] = sum_x[i+j]

b = [0] * order

for i in range(order):
    for j in range(m):
        b[i] += w[j]*(x[j]**i)*y[j]

print("A =\n", A)
print("b =", b)

x = np.linalg.solve(A, b)

print("alpha=", x)
