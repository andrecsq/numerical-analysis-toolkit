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

def inner(a, b):
    return a.T @ b

def infnorm(A):
    return np.linalg.norm(A, np.inf)

# A deve ser simétrica e definida positiva

A = np.array([[4, 1],
              [1, 3]])
b = np.array([[5],
              [4]])

check_symmetric(A)

check_positive_definite(A)

x = [np.array([[0],
               [0]])]
r = []
a = []
k = 0
eps = 0.1
max_iter = 50

while True:
    r.append(b - (A @ x[k]))
    print(f"r[{k}] =")
    print(r[k])

    # print(f"<r^k,r^k>={inner(r[k], r[k])}")
    # print(f"<r^k,Ar^k>={inner(r[k], A @ r[k])}")    
    a.append(float(inner(r[k], r[k]) / inner(r[k], A @ r[k])))
    print(f"a[{k}] =")
    print(a[k])

    x.append(x[k] + a[k]*r[k])
    print(x[k+1])

    if infnorm(x[k+1] - x[k]) < eps or k > max_iter:
        print("solution:")
        print(x[k+1])
        break

    k += 1
