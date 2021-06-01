"""
My problem and solutions

31/5/2021:  What is the bionetgen? -> Ans. other laguage
01/6/2021:  What is the environment variable BNGPATH by path? 
"""
import pysb
import bionetgen 
#import bionetgen
from pysb.simulator import ScipyOdeSimulator

from pysb import *
#pysb.pathfinder.set_path('C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/Scripts/bionetgen')
#pysb.pathfinder.set_path('C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Scripts')
#pysb.pathfinder.set_path('C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/Scripts','bionetgen')
#pysb.pathfinder.set_path('bionetgen','C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/Scripts/bionetgen')

#pysb.pathfinder.set_path('bionetgen','C:/Program Files/bionetgen')
#pysb.pathfinder.set_path(True)
#BNGPATH = pysb.pathfinder.set_path(bionetgen,'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\bionetgen\\__init__.py')
#pysb.pathfinder.set_path(bionetgen,'C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/lib/site-packages/bionetgen')
#pysb.pathfinder.set_path(bionetgen,'C:/Users/Lenovo/AppData/Local/Programs/Python/Python39/Scripts/bionetgen')
#pysb.pathfinder.set_path(bionetgen,'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\bionetgen\\__init__.py')

from pysb.integrate import Solver
Model() 
Monomer('A')
Parameter('k', 3.0)

Rule('synthesize_A', None >> A(), k)

t = [0, 10, 20, 30, 40, 50, 60]
solver = Solver(model, t)
solver.run()
print(solver.y[:, 0])


