import numpy as np
import copy

precison_low = True
gauss_seidel = True

if precison_low:
    np.set_printoptions(precision=7, suppress=True)

A = np.array([[10., -1., 1.],
              [-1., 4., -1],
              [2., -1., 5.]])
b = np.array([[11., -2., 7.]]).T

x = np.array([[0., 0., 0.]]).T

n = len(A)

max_iter = 10
eps = 0.001

print("A:\n", A)
print("b:\n", b)
print("x0:", x.T)

for it in range(max_iter):
    print(f"iter #{it}:")
    
    if gauss_seidel:
        x_new = copy.deepcopy(x)
    else:
        x_new = np.zeros(n)
        
    for i in range(n):
        s = 0
        for j in range(n):
            if i == j:
                continue
            if gauss_seidel:
                s += A[i,j]*x_new[j]
            else:
                s += A[i,j]*x[j]
        x_new[i] = (b[i] - s)/A[i,i]
    old_x = copy.deepcopy(x)
    x = np.array(x_new)
    
    print(f"x[{it}] = ", x.T)
    
    if np.amax(abs(x - old_x)) < eps:
        print("Ended")
        break

# print("\nTriangularization:")

# for i in range(n-1): # 0-indexed
        
#     for j in range(i+1, n):     
#         #print(f"{Ab[j][i]} {Ab[i][i]}")   
#         m = Ab[j][i]/Ab[i][i]        
#         print(f"m[{i},{j}] = {m}")
#         print(Ab[j] - m*Ab[i])
#         Ab[[j]] = Ab[j] - float(m)*Ab[i]
        
#     print(Ab)
