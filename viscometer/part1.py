'''
This is a new script, better than the one I was making before, all values will be outputted into the folder in which you run this script. it will also print into the console.

Everything here is for part 1 of the experiment, - the graphs

-YC
'''

import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

#defining the experimental values.
ea = []
    #first, lets define the mass & density of the balls using an array format, in order of the sheet
m = np.array([4.5886, 4.4139, 16.1327, 14.8436, 11.5499, 5.6869])
rb =np.array([2.220, 2.221, 8.124, 8.121, 8.120, 8.125])
K = np.array([0.01264, 0.10584, 0.11151, 0.76598, 7.02730, 34.31631])
    #Now, lets define the times it takes for the balls to fall through the viscometer
ts = np.array([[9.22, 9.03, 9.63, 9.03, 9.81], [11.35, 11.50, 11.50, 11.12, 11.12], [13.88, 13.69, 11.44, 11.28, 10.91], [16.97, 17.81, 21.03, 19.88, 16.94], [8.52, 8.06, 8.35, 8.53, 8.53], [19.12, 18.99, 19.37, 18.64, 18.83], [9.10, 8.84, 8.90, 8.85, 8.89], [14.41, 14.01, 14.25, 14.59, 14.61]])
    #Then the density of each of the fluids, starting with the distilled water. This is using multiple dimensions of arrays in order to sync up with the times.
rf = np.array([[1.00], [1.04], [1.08], [1.12], [1.17], [1.23], [1.29]])
con = np.array([0, 10, 20, 30, 40, 50, 60])
    #The equation we're going to use is e = K*(rb - rf)*ts
    
tu = 14.37
ru = 1.108

#Defining function
def function(K, rb, rf, ts):
    e = K*(rb - rf)*np.average(ts)
    ea.append(e)
#solving equation
function(K[1], rb[1], rf[0], ts[0])
function(K[1], rb[1], rf[1], ts[1])
function(K[1], rb[1], rf[2], ts[2])
function(K[1], rb[1], rf[3], ts[3])
function(K[2], rb[2], rf[4], ts[4])
function(K[2], rb[2], rf[5], ts[5])
function(K[3], rb[3], rf[6], ts[6])
function(K[1], rb[1], ru, tu)

print(ea)

tsav = np.array([np.average(ts[0]), np.average(ts[1]), np.average(ts[2]), np.average(ts[3]), np.average(ts[4]), np.average(ts[5]), np.average(ts[6]), np.average(ts[7])])

np.savetxt('avtimes_p1.txt', tsav, delimiter=',')
np.savetxt('viscosity_part1.txt', ea, delimiter=',')

#let's do the uncertainties.
    #calling in sympy
import sympy as sym
sym.init_printing()
    #First lets define the equation in a new fashion, f=e in this case, and d=r

C, f, k, db, df, t = sym.symbols('C f k db df t')
f = k*(db - df)*t

    #then let's differentieat them in respect to the uncertainties we have already, time and density of the fluid.

dt = sym.diff(f, t)
ddf = sym.diff(f, df)

    #Now it is time to input the values to the uncertainty equation and solve.

C = (((dt)**2)*(0.01**2) + ((ddf)**2)*(0.005**2))**(1/2)
print(C)
        # un#, where # is the percentage of the solution
un0 = C.subs({k:K[1], db:rb[1], df:rf[0], t:tsav[0]})
un10 = C.subs({k:K[1], db:rb[1], df:rf[1], t:tsav[1]})
un20 = C.subs({k:K[1], db:rb[1], df:rf[2], t:tsav[2]})
un30 = C.subs({k:K[1], db:rb[1], df:rf[3], t:tsav[3]})
un40 = C.subs({k:K[2], db:rb[2], df:rf[4], t:tsav[4]})
un50 = C.subs({k:K[2], db:rb[2], df:rf[5], t:tsav[5]})
un60 = C.subs({k:K[3], db:rb[3], df:rf[6], t:tsav[6]})
unun = C.subs({k:K[1], db:rb[1], df:ru, t:tu})
print(unun)

un = np.array([un0, un10, un20, un30, un40, un50, un60])

np.savetxt('uncertainties.txt', [un0, un10, un20, un30, un40, un50, un60], delimiter=',')
print(un0, un10, un20, un30, un40, un50, un60)

yerr = un

plt.errorbar(con, ea, yerr=un, fmt='k-', capsize=5)
plt.xlabel('Concentration of Solution / %')
plt.ylabel('Viscosity of solution / mPa s cm^3 g^(−1) s^(−1)')
plt.savefig('graph1.png')
plt.show()

#Part 1 completed no special solution done, no temperature dependence, non-newtonian fluids or graphs done yet, this will follow either in an update to this script or for the following parts.
