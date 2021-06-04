
#import pysb
#import bionetgen
#pysb.pathfinder.set_path('bng','c:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\bionetgen\\bng-win\\BNG2.pl')

from pysb import *
from pysb.integrate import Solver
model= Model()
Monomer('A')
Parameter('k', 3.0)
Rule('synthesize_A', None >> A(), k)
t = [0, 10, 20, 30, 40, 50, 60]
solver = Solver(model, t)
solver.run()
print(solver.y[:, 0])

'''
2021-06-04 21:20:05.688 - pysb.simulator.scipyode - WARNING - [test_model] This system of ODEs will be evaluated in pure Python. 
This may be slow for large models. We recommend installing the 'cython' package for compiling the ODEs to C code. 
This warning can be suppressed by specifying compiler='python'.
'''






