import sympy as sp
import numpy as np

precison_low = True

if precison_low:
    np.set_printoptions(precision=3, suppress=True)
    
eps = .001

num_equations = 2
x = [sp.Symbol(f"x_{i}") for i in range(num_equations)]

f0 = x[0]**2 + x[1]**2 - 4
f1 = x[0] - x[1]**2
print(f"f0 = {f0}")
print(f"f1 = {f1}")

F = sp.Matrix([f0,f1])
F_func = sp.lambdify((x[0], x[1]), F, modules='numpy')

J = F.jacobian([x[0],x[1]])
J_func = sp.lambdify((x[0], x[1]), J, modules='numpy')

print("Jacobian: ")
print(J)

p = np.array([[0.5],
              [1.5]])

max_iter = 10
it = 0

while True:
    print(f"\nit #{it}:")
    A = J_func(p[0,0], p[1,0]).astype(float)
    b = -F_func(p[0,0], p[1,0])
    print(f"A[{it}]=")
    print(A)
    print(f"b[{it}]= ", b.T)  
    print(f"x[{it}]= ", p.T)
    print() 
    
    y = np.linalg.solve(A, b)       
    print(f"y[{it}]= ", y.T)  
      
    error = max(y.min(), y.max(), key=abs) 
    print(f"error: {error}")
    
    p = p + y
    
    print(f"\nx[{it+1}]= ", p.T)
    
    if abs(error) < eps:
        print("Threshold reached.")
        break
    
    if it == max_iter-1:
        print("Max iterations reached.")
        break
    
    
    it+=1

# f_dx = sp.lambdify([i for i in x], sp.diff(f[0], x[0]))
#f_dx.evalf({subs={x: 1, y: 2}})
# print(f_dx(1,3))


