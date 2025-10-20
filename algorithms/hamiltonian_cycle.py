# Finding a Hamiltonian cycle in a graph (with directed edges)
# - implementation based on travelling salesperson problem
# - better implementation approach with backtracking
#
# Author: Jens Liebehenschel
# Copyright 2025

import itertools
import math
inf = math.inf
x = -inf # no path from ... to ... in adjacency matrix

# similar matrix as in dijkstra.py, but (fewer) bidirectional paths
# graph as adjacency matrix
# if names of nodes start by 1, add 1 to the index:
#     S  T  U  V  W  X  Y  Z
g = [[0, 5, 7, x, 3, 6, x, x], # node S
     [5, 0, x, 4, x, 3, 2, x], # node T
     [7, x, 0, x, 1, x, x, 2], # node U
     [x, 4, x, 0, 2, x, 1, x], # node V
     [3, x, 1, 2, 0, x, 3, 4], # node W
     [6, 3, x, x, x, 0, 1, 1], # node X
     [x, 2, x, 1, 3, 1, 0, 2], # node Y
     [x, x, 2, x, 4, 1, 2, 0]  # node Z
     ]
### graph is a line from first to last node
##g = [[0, 1, x, x, x, x, x, x], # node S
##     [x, 0, 1, x, x, x, x, x], # node T
##     [x, x, 0, 1, x, x, x, x], # node U
##     [x, x, x, 0, 1, x, x, x], # node V
##     [x, x, x, x, 0, 1, x, x], # node W
##     [x, x, x, x, x, 0, 1, x], # node X
##     [x, x, x, x, x, x, 0, 1], # node Y
##     [x, x, x, x, x, x, x, 0]  # node Z
##     ]
### graph is a line from first to last node, then back to first
##g = [[0, 1, x, x, x, x, x, x], # node S
##     [x, 0, 1, x, x, x, x, x], # node T
##     [x, x, 0, 1, x, x, x, x], # node U
##     [x, x, x, 0, 1, x, x, x], # node V
##     [x, x, x, x, 0, 1, x, x], # node W
##     [x, x, x, x, x, 0, 1, x], # node X
##     [x, x, x, x, x, x, 0, 1], # node Y
##     [1, x, x, x, x, x, x, 0]  # node Z
##     ]
### and a closed loop in the opposite direction
##g = [[0, x, x, x, x, x, x, 1], # node S
##     [1, 0, x, x, x, x, x, x], # node T
##     [x, 1, 0, x, x, x, x, x], # node U
##     [x, x, 1, 0, x, x, x, x], # node V
##     [x, x, x, 1, 0, x, x, x], # node W
##     [x, x, x, x, 1, 0, x, x], # node X
##     [x, x, x, x, x, 1, 0, x], # node Y
##     [x, x, x, x, x, x, 1, 0]  # node Z
##     ]
print(g)
for i in range(len(g)):
   for j in range(len(g)):
      print(g[i][j] if g[i][j] >= 0 else "x", end="")
   print()


# we assume the starting (and ending) node is at index 0 of g
def find_hamiltonian_cycle():
   if len(g) == 0:
      return None
   for p in itertools.permutations(range(1,len(g))):
      # check if the cycle described by p is closed
      cycle = (0,) + p + (0,)
      valid_cycle = True
      i = 0
      while valid_cycle and i < len(cycle)-1:
         if g[cycle[i]][cycle[i+1]] == x:
            valid_cycle = False
         i += 1
      # check whether cycle found
      if valid_cycle:
         return cycle
   return None

print(find_hamiltonian_cycle())
