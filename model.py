
import pysb
from pysb import *
pysb.pathfinder.set_path()
from pysb.integrate import Solver
Model() 
Monomer('A')
Parameter('k', 3.0)

Rule('synthesize_A', None >> A(), k)

t = [0, 10, 20, 30, 40, 50, 60]
solver = Solver(model, t)
solver.run()
print(solver.y[:, 0])


from pysb import *

Model()
Monomer('A')
Parameter('k', 3.0)
Rule('synthesize_A', None >> A(), k)