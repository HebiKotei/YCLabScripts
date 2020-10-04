# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:06:02 2020

@author: yc291
"""

import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import sympy as sym

sym.init_printing()

ts1 = np.array([[47.53, 48.81, 48.50, 47.72, 48.81], [31.06, 30.06, 30.04, 31.00, 29.16], [12.17, 12.27, 12.10, 11.87, 12.00]])
ts2 = np.array([[8.97, 8.81, 9.19, 9.10, 9.03], [2.56, 2.75, 2.50, 2.62, 2.62]])
tsav = []
m = 16.1327
rb = 8.124
rf = 1.579
K = 0.11151
T = np.array([25, 35, 45, 55, 65])

tsav = []
for i in range(3):
    tsav.append((np.average(ts1[i]))*2)

for i in range(2):
    tsav.append(np.average(ts2[i]))

tsav = np.array(tsav)

np.savetxt('ts3.csv', tsav, delimiter=',')

print(tsav)

visc = []

def function(ts):
    v = K*(rb - rf)*ts
    visc.append(v)

function(tsav)

visc = np.array(visc)
np.savetxt('visc3.csv', visc, delimiter=',')

C, f, r, db, df, t = sym.symbols('C f r db df t')
f = r*(db - df)*t
dt = sym.diff(f, t)
ddf = sym.diff(f, df)
C = (((dt)**2)*(0.01**2) + ((ddf)**2)*(0.005**2))**(1/2)

sig = []

for i in range(5):
    sig.append(C.subs({r:K, db:rb, df:rf, t:tsav[i]}))

sig1 = np.array(sig)

print(linregress(np.unique(1/T), np.poly1d(np.polyfit(1/T, np.log(visc[0]), 1))(np.unique(1/T))))
np.savetxt('uncertainties3.csv', sig, delimiter=',')
err = np.genfromtxt('uncertainties3.csv') / visc[0]

plt.figure()
yerr = err
plt.errorbar(1/T, np.log(visc[0]), yerr=yerr, fmt='k.', capsize=5)
plt.xlabel('1/T')
plt.ylabel('ln(Viscosity)')
plt.savefig('graph3.png')
