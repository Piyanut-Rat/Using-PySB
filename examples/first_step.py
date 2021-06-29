"""
This file is initially testing after instaaed PySB.
cite:https://pysb.readthedocs.io/en/stable/tutorial.html
"""

#import modules
from pysb import *
from pysb.integrate import Solver

#Start constaruct model
Model() 
Monomer('A')
Parameter('k', 3.0)
Rule('synthesize_A', None >> A(), k)

#Start solving
t = [0, 10, 20, 30, 40, 50, 60]
solver = Solver(model, t)
solver.run()
print(solver.y[:, 0])