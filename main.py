#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:08:52 2021

@author: jude
@edited: veelochana
"""

from pylab import *
from matplotlib.pyplot import *


f1name="hlsp_hugs_hst_wfc3-uvis-acs-wfc_ngc2808_multi_v1_catalog-meth3.txt"
F606W,F814W=np.genfromtxt(f1name,dtype=float,usecols=(20,26),unpack=True)
xp=F606W-F814W
yp=F814W
data = xp, yp

fname = "NGC2808_he33.iso"  #
V, I = np.genfromtxt(fname, dtype=float, comments="#", usecols=(10, 15), unpack=True)

dmod = 14.4
E = 0.163

# extinction
Av = 3.1 * E
Ai = 1.8 * E

Vfin = V + dmod + Av
Ifin = I + dmod + Ai

X = Vfin - Ifin
Y = Vfin

# fitting
fig, ax = subplots()
ax.scatter(xp, yp, s=0.2, marker='D', facecolors='black', edgecolors='none', label="Data")
plt.plot(X, Y, color='r', label="Best Fit")
plt.ylabel('M814')
plt.xlabel('M606 - M814')
plt.title('NGC 2808')
plt.ylim([14.5, 23])
plt.xlim([0.00, 1.5])
ax.invert_yaxis()
plt.legend()

D = (dmod + 5) / 5
D = 10 ** D
print("############ OUTPUT ###########")
print("Distance is: \n", D, "Pc")
print("Redding is :\n", E)
print("AGE is : \n10.2 Gyr")
plt.savefig('NGC2808.png', dpi=1000)
plt.show()