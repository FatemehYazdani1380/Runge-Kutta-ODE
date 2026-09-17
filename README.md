Runge-Kutta 4th Order Method for Solving a First-Order ODE

This project demonstrates how to solve a first-order ordinary differential equation (ODE) numerically using the classical fourth-order Runge-Kutta method (RK4) and compare the numerical result with the analytical solution.

Problem Description

The differential equation considered in this project is:

dydx=sin⁡(x)+y

with the initial condition:

y(0)=2

The solution is calculated in two different ways:

Numerically using the classical fourth-order Runge-Kutta method.

Analytically using SymPy.

The numerical and analytical solutions are then compared, and the absolute error is calculated for each point.

Features

Implementation of the classical RK4 numerical method

Analytical solution using SymPy

Calculation of the absolute error

Display of numerical and analytical results using a Pandas DataFrame

Calculation of the maximum absolute error

Visualization of both solutions using Matplotlib

Mathematical Method

For a first-order ODE of the form

dydx=f(x,y)

the classical RK4 method calculates four intermediate slopes:

k1=hf(xn,yn)

k2=hf(xn+h2,yn+k12)

k3=hf(xn+h2,yn+k22)

k4=hf(xn+h,yn+k3)

The next value of y is then calculated using:

yn+1=yn+k1+2k2+2k3+k46

The independent variable is updated according to:

xn+1=xn+h

Analytical Solution

For

dydx=sin⁡(x)+y

with

y(0)=2

the analytical solution is:

y(x)=32ex−12(sin⁡x+cos⁡x)

The script obtains this solution automatically using SymPy rather than hard-coding it.

Project Parameters

The default parameters used in the script are:

Parameter	Value	Description
x0	0.0	Initial value of x
xn	10.0	Final value of x
y0	2.0	Initial value y(0)
h	0.1	Step size
n	100	Number of RK4 steps

The numerical solution is therefore calculated from:

x=0

to

x=10

using a step size of:

h=0.1

Requirements

Python 3.8 or newer is recommended.

The following Python libraries are required:

NumPy

Pandas

Matplotlib

SymPy

Installation

Clone the repository:

git clone <your-repository-url>
cd <your-repository-name>


Install the required packages:

pip install numpy pandas matplotlib sympy


Alternatively, if a requirements.txt file is included:

pip install -r requirements.txt

Running the Program

Run the Python script with:

python main.py


The program will:

Calculate the numerical solution using RK4.

Calculate the analytical solution.

Calculate the absolute error.

Print a table containing the results.

Display the maximum absolute error.

Plot the numerical and analytical solutions.

Output

The program prints a table similar to:

Numerical and Analytical Solutions:

   x     y_rk4     y_exact    absolute_error
0.0   2.000000   2.000000       ...
0.1   2.210342   2.210342       ...
0.2   2.442...   2.442...       ...
...
10.0  ...        ...             ...


It also reports the maximum absolute error:

Maximum Absolute Error:
...

Visualization

The generated plot contains two curves:

Runge-Kutta 4 (RK4) — numerical solution

Analytical Solution — exact solution

Because RK4 is a fourth-order numerical method, the numerical solution should closely follow the analytical solution for a sufficiently small step size.

Error Calculation

The absolute error at each point is calculated as:

Absolute Error=∣yexact−yRK4∣

The program also determines the maximum absolute error over the entire interval.

Project Structure

A simple project structure can be:

RK4-ODE-Solver/
│
├── main.py
├── README.md
└── requirements.txt

main.py

Contains:

The ODE function

RK4 implementation

Analytical solution calculation

Error calculation

DataFrame generation

Plotting

README.md

Contains the project documentation and explanation of the numerical method.

requirements.txt

Contains the required Python dependencies.

Example:

numpy
pandas
matplotlib
sympy

Author

Fatemeh Yazdani

License

This project is intended for educational and academic purposes.
