'''

Creating a model

note: The component’s name is A, k and synthesize_A above.
'''

from pysb import *

Model()
Monomer('A')
Parameter('k', 3.0)
Rule('synthesize_A', None >> A(), k)