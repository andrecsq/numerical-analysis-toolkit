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

A = np.array([[9., -1., 0.],
              [-1., 4., 1.],
              [0., 1., 6.]])
b = np.array([[1., 0., 2.]]).T

check_symmetric(A)

check_positive_definite(A)

x = [b]
r = []
alpha = []
beta = []
v = []
k = 0
eps = 0.0001
max_iter = 2

print("A: ")
print(A)
print("b: ", b.T)

print("\nx_0 = b = ", x[0].T)

r.append(b - (A @ x[k]))
v.append(b - (A @ x[k]))
print(f"r_{k} = v_{k} = ", r[k].T)

while True:
    print(f"\niter #{k}: ")

    alpha.append(float(inner(r[k], v[k]) / inner(v[k], A @ v[k])))
    print(f"α_{k} = <r_{k},v_{k}>/<v_{k},A*v_{k}> = ", alpha[k])
    print(f"α_{k} = ({float(inner(r[k], v[k]))})/({inner(v[k], A @ v[k])}) = ", alpha[k])

    x.append(x[k] + alpha[k]*v[k])
    print(f"x_{k+1} = x_{k} + α_{k}*v_{k} = ", x[k+1].T)


    r.append(r[k] - alpha[k]*(A @ v[k]))
    print(f"r_{k+1} = r_{k} - α_{k}*(A*v_{k}) = ", r[k+1].T)

    err = infnorm(r[k+1])
    print(f'err[{k+1}] = ', err)
    if err < eps:
        print(f"Solution found on iteration #{k+1} (1-indexed): ", x[k+1].T)
        break

    beta.append(float(inner(r[k+1], A @ v[k]) / inner(v[k], A @ v[k])))
    print(f"β_{k} = <r_{k+1},A*v_{k}>/<v_{k},A*v_{k}> = ",beta[k])
    print(f"β_{k} = ({inner(r[k+1], A @ v[k])})/({inner(v[k], A @ v[k])}) = ",beta[k])

    v.append(r[k+1] - beta[k]*v[k])
    print(f"v_{k+1} = r_{k+1} - β_{k}*v_{k} = ", v[k+1].T)

    if k + 1 > max_iter:
        print(f"Max iterations reached ({max_iter}): ", x[k+1].T)
        break
    k += 1
