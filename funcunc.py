'''
Hello,

This script will be designed to allow you to commpund uncertainties in a function that would require you to use the partial derivative equation.
Please follow instructions in order to make the most out of the script and prevent it from breaking.

This is a vague script and may require you to call in additional function or continue it further, as I said in the README, the general scripts will be more simple.

You may modify this script in any fashion you like.

-YC
'''

#calling packages & initialising
import sympy as sym
import numpy as np

sym.init_printing()

#definitions, pLease add additional symbols to fit your equations.
#Please ensure to add them onto the left hand side of the equals sign, seperate them with commas.
#Then in the 'string', add the symbol again.
a, b, c, x, y, z = sym.symbols('a b c x y z')
'''
any constants in the equation can be definined below as shown:
    g = 9.81
    e = 1.602*10**(-19)
'''

#Define your equation with two variables. This example will be here
y = 2*x*z
dx = sym.diff(y, x).doit() #1
dz = sym.diff(y, z).doit() #2

print('your partial derivatives are:')
print('dy/dx =', dx)
print ('dy/dz =', dz)

#using the formula for the compounding of uncertainties for a function with two unknown values.
#input values in the console for your absolute uncertainties, it'll ask for dx first in the example, then dz's uncertainty

print('Please input the values for the absolute uncertainty of the first variable you are differentiating respect to')
ux = float(input())
print('Please input the values for the absolute uncertainty of the second variable you are differentiating respect to')
uz = float(input())

eq = ((dz**2)*(uz**2)) + ((dx**2)*(ux**2))

