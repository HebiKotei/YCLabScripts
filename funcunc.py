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

sym.init_printing()

#definitions, pLease add additional symbols to fit your equations. Please ensure to add them onto the left hand side of the equals sign, seperate them with commas. Then in the string, add the symbol again.
a, b, c, x, y = symbols('a b c x y')
