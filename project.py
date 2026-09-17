"""
Runge-Kutta 4th Order Method for Solving a First-Order ODE

This script solves the differential equation:

    dy/dx = sin(x) + y

using the classical fourth-order Runge-Kutta (RK4) method
and compares the numerical solution with the analytical solution.

Author: Fatemeh Yazdani
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sympy import Eq, Function, dsolve, lambdify, sin, symbols


def f(x, y):
    """
    Define the first-order differential equation.

    dy/dx = sin(x) + y

    Parameters:
    x : float
        Independent variable.
    y : float
        Dependent variable.
    float
        Value of dy/dx.
    """
    return np.sin(x) + y


def runge_kutta_4(x0, y0, h, n):
    """
    Solve an ODE using the classical fourth-order Runge-Kutta method.

    Parameters:
    x0 : float
        Initial value of x.
    y0 : float
        Initial value of y.
    h : float
        Step size.
    n : int
        Number of steps.
    list of tuple
        Numerical solution as (x, y) pairs.
    """
    results = []

    x = x0
    y = y0

    for _ in range(n + 1):
        results.append((x, y))

        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

    return results


def analytical_solution(y0):
    """
    Calculate the analytical solution of the ODE using SymPy.

    Parameters:
    y0 : float
        Initial condition y(0) = y0.
    function
        Numerical function representing the analytical solution.
    """
    x = symbols("x")
    y = Function("y")

    equation = Eq(
        y(x).diff(x),
        sin(x) + y(x)
    )

    solution = dsolve(
        equation,
        y(x),
        ics={y(0): y0}
    )

    return lambdify(x, solution.rhs, modules="numpy")


def main():
    """Run the numerical and analytical solution comparison."""

    # Problem parameters
    x0 = 0.0
    xn = 10.0
    y0 = 2.0
    h = 0.1

    # Calculate the number of steps
    n = int(round((xn - x0) / h))

    # Numerical solution using RK4
    results = runge_kutta_4(x0, y0, h, n)

    # Convert numerical results to DataFrame
    df = pd.DataFrame(
        results,
        columns=["x", "y_rk4"]
    )

    # Analytical solution
    y_exact = analytical_solution(y0)

    x_values = np.linspace(x0, xn, n + 1)
    y_exact_values = y_exact(x_values)

    # Add analytical solution and absolute error to DataFrame
    df["y_exact"] = y_exact_values
    df["absolute_error"] = np.abs(df["y_exact"] - df["y_rk4"])

    # Display results
    print("\nNumerical and Analytical Solutions:\n")
    print(df.to_string(index=False))

    print("\nMaximum Absolute Error:")
    print(f"{df['absolute_error'].max():.6e}")

    # Plot results
    plt.figure(figsize=(10, 6))

    plt.plot(
        df["x"],
        df["y_rk4"],
        label="Runge-Kutta 4 (RK4)",
        linewidth=2
    )

    plt.plot(
        df["x"],
        df["y_exact"],
        label="Analytical Solution",
        linestyle="--",
        linewidth=2
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("RK4 Numerical Solution vs Analytical Solution")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
