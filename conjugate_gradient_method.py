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

A = np.array([[8, 1, 1],
              [1, 6, -1],
              [1, -1, 4]])
b = np.array([[2, 3, -4]]).T

check_symmetric(A)

check_positive_definite(A)

x = [b]
r = []
alpha = []
beta = []
v = []
k = 0
eps = 0.1
max_iter = 50

print("A: ")
print(A)
print("b: ")
print(b)

print("Aprox inicial: x[0] = b")

r.append(b - (A @ x[k]))
v.append(b - (A @ x[k]))
print(f"r[{k}] = v[{k}] =")
print(r[k])

while True:

    alpha.append(float(inner(r[k], v[k]) / inner(v[k], A @ v[k])))
    print(f"alpha[{k}] =")
    print(alpha[k])

    x.append(x[k] + alpha[k]*v[k])
    print(f"x[{k+1}] =")
    print(x[k+1])

    r.append(r[k] - alpha[k]*(A @ v[k]))
    print(f"r[{k+1}] =")
    print(r[k+1])

    if infnorm(r[k+1]) < eps:
        print(f"Solution found on iteration #{k+1} (1-indexed):")
        print(x[k+1])
        break

    beta.append(float(inner(r[k+1], A @ v[k]) / inner(v[k], A @ v[k])))
    print(f"beta[{k}] =")
    print(beta[k])

    v.append(r[k+1] - beta[k]*v[k])
    print(f"v[{k+1}] =")
    print(v[k+1])

    if k + 1 > max_iter:
        print("Solution after {max_iter} iterations:")
        print(x[k+1])
        break

    k += 1
