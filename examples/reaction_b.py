'''

Model creation in depth

'''
from pysb import *

Model()
Monomer('Raf', ['s', 'k'], {'s': ['u', 'p']})
Monomer('MEK', ['s218', 's222', 'k'], {'s218': ['u', 'p'], 's222': ['u', 'p']})
'''
Now let’s provide a definition for MEK, the substrate of Raf. 
MEK has two serine residues at positions 218 and 222 in the amino acid sequence which are both phosphorylated by Raf. 
We can’t call them both s as site names must be unique within a monomer, 
so we’ve used the residue numbers in the sites’ names to distinguish them: s218 and s222. 
MEK has a kinase domain of its own for which we’ve again used k:

cite: https://pysb.readthedocs.io/en/stable/tutorial.html
'''