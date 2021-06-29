'''
This line cite from Lopez, C. F., Muhlich, J. L., Bachman, J. A., & Sorger, P. K. (2013). Programming biological models in Python using PySB. Molecular systems biology, 9(1), 646.
 or opening with https://www.embopress.org/doi/full/10.1038/msb.2013.1
'''

from pysb import *
from pysb.integrate import odesolve
from pylab import plot, linspace

Model()

#Declare the monomers
Monomer('L', ['s']) # L is name of protein and s is name of site
Monomer('R', ['s']) # R is name of protein and s is name of site

#Declare the parameters
Parameter('kf', 1e-3) # forward rate
Parameter('kr', 1e-3) # reward rate

#Declare the initial conditions (empty binding)
Initial(L(s = None), Parameter('L_0', 100)) # None mean empty binding sites s that the initial L protein (L0) is 100.
Initial(R(s = None), Parameter('R_0', 200)) # None mean empty binding sites s that the initial R protein (R0) is 200.

#Declare the binding rule
Rule('L_binds_R', 
    L(s = None) + R(s = None) |  L(s = 1) % R(s = 1), # L(s = 1) % R(s = 1) that  shares a single ‘bond’. Note this line is rate equation.
    kf,kr)

# Observe the model
Observable('LR', L(s = 1) % R(s = 1))

# Simulate the model
time = linspace(0, 40)
x = odesolve(model, time)

plot(time, x['LR'])



'''
2021-06-29 21:14:28.098 - pysb.simulator.scipyode - WARNING - [Hello_world] This system of ODEs will be evaluated in pure Python. This may be slow for large models. We recommend installing the 'cython' 
package for compiling the ODEs to C code. This warning can be suppressed by specifying compiler='python'


### After pip install Cython on command -> still WARNING (?)
'''
