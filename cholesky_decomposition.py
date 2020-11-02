import numpy as np

def check_symmetric(A, rtol=1e-05, atol=1e-08):
    is_symmetric = np.allclose(A, A.T, rtol=rtol, atol=atol)

    if (not is_symmetric):
        print("A is not symmetric")
        quit()

def check_positive_definite(A):
    try:
        _ = np.linalg.cholesky(A)
    except:
        print("A is not positive definite")
        quit()
        
def cholesky_decomposition(A):
    n = A.shape[0]    
    L = np.identity(n)

    L[0,0]=(A[0,0])**(1/2)
    print(f"L[0,0] = A[0,0]({A[0,0]})^(1/2) = {L[0,0]}")

    for j in range(1, n):
        L[j,0] = A[j,0]/L[0,0]
        print(f"L[{j},0] = A[{j},0]({A[j,0]})/L[0,0]({L[0,0]}) = {L[j,0]}")
    print()

    for i in range(1,n-1):
        s = 0
        for k in range(i):
            s += float(L[i,k]**2)            
        L[i,i] = (A[i,i] - s)**(1/2)
        print(f"L[{i},{i}] = (A[{i},{i}]({A[i,i]}) - s({s}))^(1/2) = {L[i,i]}")        
        print()
        
        for j in range(i+1,n):
            s = 0
            for k in range(i):
                s += float(L[j,k]*L[i,k])                
            L[j,i] = (A[j,i] - s)/L[i,i]
            print(f"L[{j},{i}] = (A[{j},{i}]({A[j,i]}) - s({s}))/L[{i},{i}]({L[i][i]}) = {L[j,i]}")            
        print()
        
        s = 0
        for k in range(n-1):
            s += float(L[n-1,k]**2) 
        L[n-1,n-1] = (A[n-1,n-1] - s)**(1/2)
        print(f"L[{n-1},{n-1}] = (A[{n-1},{n-1}]({A[n-1,n-1]}) - s({s}))^(1/2) = {L[n-1,n-1]}")
    
    return L
    
# A deve ser simétrica e definida positiva

# A = np.array([[4, -1, 1],
#             [-1, 4.25, 2.75],
#             [1, 2.75, 3.5]])

A = np.array([[6, 2, 1, -2],
              [2, 8, -1, -1],
              [1, -1, 5, 1],
              [-2, -1, 1, 6]])

check_symmetric(A)

check_positive_definite(A)

print("A: ")
print(A)
print()

L = cholesky_decomposition(A)
    
print()
print("L =")
print(L)
print("L^t =")
print(L.T)