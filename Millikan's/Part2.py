#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
For Millikan's Oil Droplet Experiment. Leybold Didactic scripts.

Just input the data you have gained for the fall/rise time in tf & tr.
Do not forget to check that 's' is the same value for the fall./rise distance that you have performed.
This does not do both polarities of the oil droplet, you'll have to run the code seperately with the different values.

-YC
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import optimize
import sympy as sym

V = np.array([612, 149, 206, 177, 267, 267, 374, 194, 223, 327, 242, 369])
tf = np.array([137, 118, 78, 86, 28, 125, 98, 27, 86, 39, 72, 67])
tr = np.array([35, 39, 16, 27, 41, 25, 37, 28, 56, 71, 6, 20])
g = 9.80665
do = 871
da = 1.161
na = 18.6*10**(-6)
d = 6.00*10**(-3)
s = 4.00*10**(-3)
e = 1.602*10**(-19)
a = 0.07776*10**(-6)

sym.init_printing(use_unicode=True)

#Starting with the velocity
vf = s/tf
print(vf)
np.savetxt('velocity.txt', vf, delimiter=',')

vr = s/tr
print(vr)
np.savetxt('risevel.txt', vr, delimiter=',')

#calculating the error for the velocity

sig_t = 0.5
sig_d = 0.05*10**(-3)

    #fall velocity
(uncv) = (vf)*((((sig_t)/tf)**2)+(((sig_d)/s)**2))**(1/2)
print(uncv)
np.savetxt('uncvf.txt', uncv, delimiter=',')

    #rise velocity
(unvr) = (vr)*((((sig_t)/tr)**2)+(((sig_d)/s)**2))**(1/2)
print(unvr)
np.savetxt('unvr.txt', unvr, delimiter=',')

#Now going onto the radius of the oil droplet
    #Defining the equation used.
r = ((9*na*vf)/(2*(do-da)*g))**(1/2)
print(r)
np.savetxt('radius.txt', r,delimiter=',')
    #Managing the uncertainty
        #The uncertainty will remain the same as calulcated for the velocities
        #due to the fact that there is not compunding with other uncertainties

#Moving onto the charge on the droplet
    #define the equation
q, Vo, vfa, vri = sym.symbols('q Vo vfa vri')
q = ((18*sym.pi*d)/Vo)*(((((na**3)*vfa)/(2*(do - da)*g)))**(1/2))*(vfa+vri)

plt.plot(vr, vf)
plt.show()
