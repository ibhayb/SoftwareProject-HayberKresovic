# Finding an Eulerian cycle in a graph
# Using Hierholzer's algorithm
# Graph is given by an adjacency list with directed unweighted edges
# Important note:
# - Eulerian cycle means that every edge is traversed once
# - If a node is not connected to the graph, then it is also not included in the Eulerian cycle
# - This is not checked in the code to keep it shorter
# 
# Author: Jens Liebehenschel
# Copyright 2025

# graph as adjacency list, here without weigths
# This is based on the adjacency matrix as in dijkstra.py (without weights)
# Edges: start->end, i.e. 0->1, 0->2, ...
g = [[1,2,3,4,5],
     [3,5,6],
     [4,7],
     [2,4,6],
     [6,7],
     [6],
     [7],
     [5]
     ]
## respective adjaceny matrix:
##g = [[0, 4, 7, 5, 3, 6, x, x], # node S
##     [x, 0, x, 4, x, 3, 2, x], # node T
##     [x, x, 0, x, 1, x, x, 2], # node U
##     [x, x, 1, 0, 2, x, 1, x], # node V
##     [x, x, x, x, 0, x, 1, 4], # node W
##     [x, x, x, x, x, 0, 1, x], # node X
##     [x, x, x, x, x, x, 0, 2], # node Y
##     [x, x, x, x, x, 1, x, 0]  # node Z
##     ]
#
g = [[1],
     [2],
     [3],
     [0,4],
     [5],
     [3]
     ]
#
g = [[1],
     [2,6],
     [0],
     [4,7],
     [5],
     [3],
     [3],
     [1]
     ]
#
g = [[1],
     [0]
     ]
#
g = [[1,1],
     [0,0]
     ]
#
g = [[1,2],
     [0],
     [0]
     ]
#
g = [[1],
     [2],
     [3],
     [0]
     ]
#
g = [[1,1],
     [2,0],
     [3],
     [0]
     ]
#
g = [[1,1,2],
     [0,2],
     [3,3,0],
     [2,0]
     ]
#
g = [[1,2],
     [0,2],
     [3,3,0],
     [2,0]
     ]

# False cannot be used as (internal) return values, since there is a node 0 and False == 0
# We use -1 and [-1] instead

# find an edge that is connected to one node in l
# -1 -> no new starting node found
def get_first_edge_start(g,l):
   for start in l:
      if len(g[start]) > 0:
         return start
   return -1

# calculate a new sub cycle starting at node i
# [-1] -> no new cycle detected
def get_new_cycle(g,i):
   end = -1
   new_cycle = [i]
   while end != i:
      if len(g[new_cycle[-1]]) == 0:
         return [-1]
      end = g[new_cycle[-1]].pop(0)
      new_cycle += [end]
   return new_cycle

def find_eulerian_cycle(adj_list):
   # use a copy of the graph's adjacency list
   # it will be destroyed, since the algorithms removes edges
   g = [end[:] for end in adj_list]

   complete_cycle = [0]
   new_cycle = get_new_cycle(g,0)
   while new_cycle[0] != -1:
      #integrate new cycle into the existing one
      i = complete_cycle.index(new_cycle[0])
      complete_cycle = complete_cycle[:i] + new_cycle + complete_cycle[i+1:]
      start = get_first_edge_start(g,complete_cycle)
      if start == -1 and any([len(g[i])>0 for i in range(len(g))]):
         return False
      else:
         new_cycle = get_new_cycle(g,start)
   if any([len(g[i])>0 for i in range(len(g))]):
      return "Eulerian cycle not found"
   else:
      return complete_cycle

print(find_eulerian_cycle(g))


