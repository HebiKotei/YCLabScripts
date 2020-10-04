'''
Part 2 - Calculating the dynamic viscosity for the 40% solution,
'''
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.stats import linregress

sym.init_printing()

ts = np.array([[60.53, 60.09, 60.79, 60.40, 60.48], [60.37, 60.88, 59.67, 59.70, 60.24], [60.11, 60.61, 59.13, 61.16, 59.87], [59.22, 59.26, 59.24, 59.88, 59.96], [59.41, 59.45, 58.90, 57.63, 58.98]])
tsav =  []
T = np.array([25 + 273.15, 35 + 273.15, 45 + 273.15, 55 + 273.15, 65 + 273.15])
m = 4.4139
rb = 2.221
K = 0.10584
rf = 1.71
visc = []

for i in range(5):
    tsav.append(np.average(ts[i]))

tsav = np.array(tsav)

np.savetxt('part2tsav.txt', tsav, delimiter=',')

def function(ts):
    v = K*(rb - rf)*tsav
    visc.append(v)


function(tsav)

visc = np.array(visc)
np.savetxt('part2visc.txt', visc, delimiter=',')

C, f, r, db, df, t = sym.symbols('C f r db df t')
f = r*(db - df)*t
dt = sym.diff(f, t)
ddf = sym.diff(f, df)
C = (((dt)**2)*(0.01**2) + ((ddf)**2)*(0.005**2))**(1/2)

sig = []

for i in range(5):
    sig.append(C.subs({r:K, db:rb, df:rf, t:tsav[0]}))

sig1 = np.array(sig)

print(linregress(np.unique(1/T), np.poly1d(np.polyfit(1/T, np.log(visc[0]), 1))(np.unique(1/T))))

np.savetxt('uncertainties2.csv', sig, delimiter=',')

err = np.genfromtxt('uncertainties2.csv') / visc[0]

plt.figure()
yerr = err
plt.errorbar(1/T, np.log(visc[0]), yerr=yerr, fmt='k.', capsize=2)
plt.plot(np.unique(1/T), np.poly1d(np.polyfit(1/T, np.log(visc[0]), 1))(np.unique(1/T)), 'r')
plt.xlabel('1/T')
plt.ylabel('ln(Viscosity)')
plt.savefig('graph2.png')
