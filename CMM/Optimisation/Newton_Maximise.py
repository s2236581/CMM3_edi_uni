import numpy as np
import matplotlib.pyplot as plt

# Define the target function to be optimized
def f(x):
    return x**3 - 6*x**2 + 4*x + 2

# Plot the target function
x = np.linspace(-1, 1)
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()

# Define the first and second derivatives of the target function
def fprime(x):
    return 3*x**2 - 12*x + 4

def fsecond(x):
    return 6*x - 12

# Define a quadratic approximation based on a point and its derivatives
def quadratic_approx(x, x0, f, fprime, fsecond):
    return f(x0) + fprime(x0)*(x - x0) + 0.5*fsecond(x0)*(x - x0)**2

# Plot the target function and its quadratic approximation
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, 0, f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-2, 3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.legend()

# Implement the Newton-Raphson method for finding the maximum
def newton(x0, fprime, fsecond, maxiter=100, eps=0.0001):
    x = x0
    for i in range(maxiter):
        xnew = x - (fprime(x) / fsecond(x))
        if abs(xnew - x) < eps:
            return xnew  # Return the x-coordinate of the maximum if convergence is achieved
        x = xnew
    return x  # Return the last estimate if maximum iterations are reached

# Find the x-coordinate of the maximum using the Newton-Raphson method
x_max = newton(0, fprime, fsecond)
print("x-coordinate of the maximum:", x_max)

# Plot the result with the maximum highlighted
fig, ax = plt.subplots()
ax.plot(x, f(x), label='target')
ax.grid()
ax.plot(x, quadratic_approx(x, x_max, f, fprime, fsecond), color='red', label='quadratic approximation')
ax.set_ylim([-2, 3])
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.axvline(x=x_max, color='green', label='maximum')
plt.legend()

plt.show()
