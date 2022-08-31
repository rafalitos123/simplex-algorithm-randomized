import gilp
import numpy as np
from gilp.simplex import LP, simplex
from gilp.examples import KLEE_MINTY_3D_LP
# This is a simple example on how to run the simplex algorithm with
# the random-edge pivot rule as described in the paper:
# https://www.mi.fu-berlin.de/math/groups/discgeom/ziegler/Preprintfiles/038a-PREPRINT.pdf
# Note: this paper alse describes the Kalai's random-facet algorithm

A = np.array([[2, 1, 3],
              [1, 1, 2],
              [1, 0, 4]])
b = np.array([[20],
              [16],
              [7]])
c = np.array([[5],
              [3],
              [2]])
lp = LP(A,b,c)

from gilp.visualize import simplex_visual

# Basic example
print("Showing basic example on browser")
print("")
simplex_visual(lp, rule='dantzig').show()

# KLEE_MINTY example
print("Showing Klee-Minty 3D cube (dantzig vs random-edge) on browser")
print("")
simplex_visual(KLEE_MINTY_3D_LP, rule='dantzig').show()
simplex_visual(KLEE_MINTY_3D_LP, rule='random-edge').show()

# Let's now run some comparisons, between random-edge and bland pivot rule

def compare_pivot_rules(lp, name):
    print(f"Running Simplex algorithm on case {name}:")
        
    bland_simplex_res = simplex(lp, pivot_rule='bland')
    bland_path = bland_simplex_res.path
    print(f"With Bland rule: {len(bland_path)} pivots")

    dantzig_simplex_res = simplex(lp, pivot_rule='dantzig')
    dantzig_path = dantzig_simplex_res.path
    print(f"With Dantzig rule: {len(dantzig_path)} pivots")

    random_edge_results = []
    for i in range(10):
        random_edge_res = simplex(lp, pivot_rule='random-edge')
        random_edge_path = random_edge_res.path
        random_edge_results.append(len(random_edge_path))
    print(f"With Randon-Edge rule: {sum(random_edge_results) / len(random_edge_results)} pivots (average over 10 executions)")
    print("")

print("Running dantzig, bland and random-edge simplex algorithm for various examples and compare results")
print("")
RANDOM_INTEGER_7D_LP = LP(np.array([
                                 [1,0,0,0, 1,2,3],
                                 [1,0,0,1, 41,10,3],
                                 [1,0,1,0, 1,2,3],
                                 [1,0,1,1, 12,2,3],
                                 [1,1,0,0, 30,2,3],
                                 [1,1,0,1, 1,400,3],
                                 [1,0,3,0, 1,0,4],
                                 [0,0,6,1, 1,80,3]
                                ]),
                       np.array([[6],[8],[5],[8], [9], [11], [13], [50]]),
                       np.array([[1],[2],[4], [5], [6], [7], [9]]))

compare_pivot_rules(RANDOM_INTEGER_7D_LP, 'RANDOM_INTEGER_7D_LP')

all_lp_examples = dict()
for name, obj_ in gilp.examples.__dict__.items():
    if isinstance(obj_, LP):
        compare_pivot_rules(obj_, name)
