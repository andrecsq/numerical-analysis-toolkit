# Numerical Analysis Toolkit

This repository contains implementations of various numerical methods algorithms in Python, developed as part of the Numerical Methods discipline at the Federal University of Rio de Janeiro (UFRJ).

## 📋 Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Algorithms Implemented](#algorithms-implemented)
  - [Linear Systems](#linear-systems)
  - [Matrix Decomposition](#matrix-decomposition)
  - [Interpolation](#interpolation)
  - [Optimization](#optimization)
  - [Nonlinear Systems](#nonlinear-systems)
  - [Curve Fitting](#curve-fitting)
- [Usage Examples](#usage-examples)
- [Installation](#installation)

## 🔍 Overview

This collection implements fundamental numerical methods for solving linear systems, matrix decomposition, interpolation, optimization, and curve fitting problems. Each implementation includes detailed step-by-step calculations and is designed for educational purposes.

## 📦 Requirements

- **Python 3.x**
- **NumPy** - For numerical computations
- **SymPy** - For symbolic mathematics (used in some algorithms)

## 🧮 Algorithms Implemented

### Linear Systems

#### 1. **Gaussian Elimination** (`gauss_elimination.py`)
Solves linear systems using Gaussian elimination with optional partial pivoting.

**Features:**
- Forward elimination with pivoting
- Back substitution
- Support for polynomial evaluation
- Configurable precision output

**Algorithm:** Transforms the augmented matrix to row echelon form, then solves via back substitution.

#### 2. **Gauss-Jacobi Method** (`gauss_jacobi.py`)
Iterative method for solving linear systems, with optional Gauss-Seidel variant.

**Features:**
- Jacobi iteration (default)
- Gauss-Seidel iteration (configurable)
- Convergence checking
- Maximum iteration limit

**Algorithm:** Iteratively improves solution using: `x[i]^(k+1) = (b[i] - Σ(a[ij]*x[j]^k)) / a[ii]`

### Matrix Decomposition

#### 3. **Cholesky Decomposition** (`cholesky_decomposition.py`)
Decomposes symmetric positive-definite matrices into L*L^T form.

**Features:**
- Symmetry and positive-definiteness validation
- Step-by-step decomposition calculation
- Lower triangular matrix output

**Requirements:** Matrix must be symmetric and positive-definite.

#### 4. **Crout Decomposition** (`crout_decomposition.py`)
Performs LDLT decomposition for symmetric matrices.

**Features:**
- Symmetry validation
- Computes L (lower triangular) and D (diagonal) matrices
- Detailed calculation steps

**Algorithm:** Decomposes A = L*D*L^T where L is unit lower triangular and D is diagonal.

### Interpolation

#### 5. **Hermite Interpolation** (`hermite.py`)
Constructs polynomial interpolation using both function values and derivatives.

**Features:**
- Uses function values and first derivatives
- Symbolic polynomial construction
- Polynomial evaluation at specific points
- Derivative calculation

**Algorithm:** Constructs cubic polynomial using Hermite basis functions φ and ψ.

### Optimization

#### 6. **Gradient Method** (`gradient_method.py`)
Implements steepest descent for solving linear systems Ax = b.

**Features:**
- Symmetry and positive-definiteness validation
- Optimal step size calculation
- Convergence monitoring
- Infinity norm error checking

**Algorithm:** `x^(k+1) = x^k + α_k * r^k` where `α_k = <r^k,r^k>/<r^k,A*r^k>`

#### 7. **Conjugate Gradient Method** (`conjugate_gradient_method.py`)
Advanced iterative method for solving symmetric positive-definite linear systems.

**Features:**
- Matrix property validation
- Conjugate direction vectors
- Optimal step size and direction calculation
- Detailed iteration output

**Algorithm:** Combines steepest descent with conjugate directions for faster convergence.

### Nonlinear Systems

#### 8. **Newton's Method for Nonlinear Systems** (`nonlinear_systems.py`)
Solves systems of nonlinear equations using Newton-Raphson method.

**Features:**
- Symbolic Jacobian computation
- Automatic differentiation using SymPy
- Convergence monitoring
- Maximum iteration limit

**Example System:**
- f₀(x₀,x₁) = x₀² + x₀x₁² + 1
- f₁(x₀,x₁) = x₀x₁ + x₁² - 2

### Curve Fitting

#### 9. **Weighted Least Squares (MMQ)** (`mmq.py`)
Fits polynomial curves to data points using weighted least squares.

**Features:**
- Weighted data point fitting
- Configurable polynomial order
- Normal equation solution
- Coefficient calculation

**Algorithm:** Minimizes weighted sum of squared errors: `Σ w[i](p(x[i]) - y[i])²`

## 🚀 Usage Examples

### Gaussian Elimination
```python
import numpy as np
from gauss_elimination import *

A = np.array([[7, 7.6, 11.88],
              [7.6, 11.88, 19.144],
              [11.88, 19.144, 31.837]])
b = np.array([[4.9, 7.82, 12.866]]).T

# The script will solve Ax = b and output the solution
```

### Cholesky Decomposition
```python
import numpy as np
from cholesky_decomposition import *

A = np.array([[10., 1., 0.],
              [1., 10., 1.],
              [0., 1., 10.]])

# Automatically checks if A is symmetric and positive-definite
L = cholesky_decomposition(A)
```

### Conjugate Gradient Method
```python
import numpy as np
from conjugate_gradient_method import *

A = np.array([[9., -1., 0.],
              [-1., 4., 1.],
              [0., 1., 6.]])
b = np.array([[1., 0., 2.]]).T

# The algorithm will iterate until convergence
```

## 💻 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/numerical-methods-algorithms.git
cd numerical-methods-algorithms
```

2. **Install required dependencies:**
```bash
pip install numpy sympy
```

3. **Run any algorithm:**
```bash
python gauss_elimination.py
python cholesky_decomposition.py
# ... etc
```

## 📚 Educational Notes

Each implementation includes:
- **Detailed comments** explaining each step
- **Mathematical formulations** in code comments
- **Convergence criteria** and error checking
- **Input validation** where applicable
- **Step-by-step output** for learning purposes

These algorithms are designed for **educational purposes** and may not be optimized for large-scale production use. They prioritize clarity and understanding over performance.

## 🎓 Academic Context

These implementations were developed as part of coursework for the Numerical Methods discipline at UFRJ (Federal University of Rio de Janeiro). They demonstrate fundamental concepts in:

- **Linear Algebra** (matrix operations, decompositions)
- **Numerical Analysis** (convergence, stability, error analysis)
- **Optimization** (gradient-based methods)
- **Interpolation Theory** (polynomial fitting)
- **Computational Mathematics** (algorithmic implementations)

## ⚠️ Notes

- Most algorithms include **validation checks** for input matrices (symmetry, positive-definiteness)
- **Convergence tolerances** are configurable in most iterative methods
- Output **precision can be adjusted** using NumPy print options
- Some algorithms include **debugging output** for educational purposes

---

*For questions or improvements, please feel free to contribute or reach out!*
