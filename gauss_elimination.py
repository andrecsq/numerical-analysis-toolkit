import numpy as np

def pivot(i):
    pivot_row_index = i
    for k in range(i+1, len(Ab)):
        if Ab[k][i] > Ab[pivot_row_index][i]:
            pivot_row_index = k

    if Ab[i][i] == Ab[pivot_row_index][i]:
        print("No pivot needed")
    else:
        print(f"L_{i}({Ab[i][i]}) <-> L_{pivot_row_index}({Ab[pivot_row_index][i]})")
    
    Ab[[i, pivot_row_index]] = Ab[[pivot_row_index, i]]   
    

A = np.array([[.02, .01, 0., 0.],
              [1., 2., 1., 0.],
              [0., 1., 2., 1.],
              [0., 0., 100., 200.]])
b = np.array([[0.02, 1, 4, 800]]).T

pivot_enabled = True
precison_low = True

if precison_low:
    np.set_printoptions(precision=3, suppress=True)

print("Initial value:")
Ab = np.concatenate((A,b), axis=1)
n = len(Ab)
print(Ab)

print("\nTriangularization:")

for i in range(n-1): # 0-indexed

    print(f"\nit #{i+1}:")    
    if (pivot_enabled):
        pivot(i) 
        print(Ab)
        print()
        
    for j in range(i+1, n):     
        #print(f"{Ab[j][i]} {Ab[i][i]}")   
        m = Ab[j][i]/Ab[i][i]        
        print(f"m[{i},{j}] = {m}")
        print(Ab[j] - m*Ab[i])
        Ab[[j]] = Ab[j] - float(m)*Ab[i]
        
    print(Ab)
    
print("\nAb is triangular")
print("\nStarting backsubstitution:")

x = [0]*n
for i in reversed(range(n)):
    s = np.inner(Ab[i, 0:n], x)
    x[i] = (Ab[i, n] - s)/Ab[i][i]
    print(f"x[{i}] = (Ab[{i},{n}]({Ab[i, n]}) - sum(a_{i}j,x_j)({s}))/A[{i},{i}]({A[i,i]}) = {x[i]}")
    #x = Ab[i, n] - Ab[i,0:n-2]
  
print("\nx: ")  
print(x)
    
    
