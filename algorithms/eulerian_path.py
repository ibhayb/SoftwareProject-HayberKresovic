# Finding an Eulerian path in a graph
# Using Hierholzer's algorithm
# Graph is given by an adjacency matrix with undirected unweighted edges
#
# Author: Jens Liebehenschel
# Copyright 2025

# graph as adjacency matrix, number of edges between nodes specified
# This is the adjacency matrix as in dijkstra.py (without weights)
#     S  T  U  V  W  X  Y  Z
g = [[0, 1, 1, 1, 1, 1, 0, 0], # node S
     [0, 0, 0, 1, 0, 1, 1, 0], # node T
     [0, 0, 0, 0, 1, 0, 0, 1], # node U
     [0, 0, 1, 0, 1, 0, 1, 0], # node V
     [0, 0, 0, 0, 0, 0, 1, 1], # node W
     [0, 0, 0, 0, 0, 0, 1, 0], # node X
     [0, 0, 0, 0, 0, 0, 0, 1], # node Y
     [0, 0, 0, 0, 0, 1, 0, 0]  # node Z
     ]

#
g = [[0, 2, 1, 1],
     [2, 0, 1, 0],
     [2, 1, 0, 3],
     [1, 0, 3, 0]
     ]

#
g = [[0, 2, 2, 1],
     [2, 0, 1, 0],
     [2, 1, 1, 3],
     [1, 0, 3, 0]
     ]
#
g = [[0, 2, 2, 1],
     [2, 0, 1, 0],
     [2, 1, 0, 4],
     [1, 0, 4, 0]
     ]
#
g = [[0, 2, 2, 1],
     [2, 0, 1, 0],
     [2, 1, 0, 3],
     [1, 0, 3, 0]
     ]

#
g = [[0, 2, 2, 2],
     [2, 0, 2, 0],
     [2, 2, 0, 3],
     [2, 0, 3, 0]
     ]

#
g = [[0, 1, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0],
     [0, 1, 0, 2, 2, 1],
     [0, 0, 2, 0, 1, 1],
     [0, 0, 2, 1, 0, 0],
     [0, 0, 1, 1, 0, 0]
     ]

# False cannot be used as (internal) return values, since there is a node 0 and False == 0
# We use -1 and [-1] instead

def initial_checks_ok(g):
   # Check whether graph is undirected, i.e. check whether edges are symmetric
   # check diagonal
   for start in range(len(g)):
      if g[start][start] != 0:
         print("Graph has edge from node", start, "to itself")
         return -1
   # check for symmetry, iterate over upper right triangular matrix
   for start in range(len(g)):
      for end in range(start+1,len(g)):
         if g[start][end] != g[end][start]:
            print("Graph not symmetric, edge between nodes", start, "and", end)
            return -1

   # Check in advance whether an Eulerian path exists.
   # Two conditions need to be fulfilled
   # Two node degrees are odd (start_node and end_node)
   # All other node degrees are even (0 is accepted, i.e. isolated node)
   start_node = -1
   end_node = -1
   for i in range(len(g)):
      if sum(g[i]) % 2 == 1:
         if start_node == -1:
            start_node = i
         elif end_node == -1:
            end_node = i
         else:
            print("More than two nodes with odd node degrees, Eulerian path does not exist")
            return -1
   if start_node == -1:
      print("Only nodes with even node degrees found, Eulerian cycle exists")
      return -1
   return start_node

# find an edge that is connected to node start in g and remove edge
# -1 -> no new node found
def get_next_node_delete_edge(g,start):
   for end in range(len(g)):
      if g[start][end] > 0:
         g[start][end] -= 1
         g[end][start] -= 1
         return end
   return -1

# find first edge in graph
def find_first_edge(g):
   for start in range(len(g)):
      if sum(g[start]) > 0:
         return start
   return [-1]

# calculate a new sub path or cycle, i.e. traverse edges as log as this is possible
# if start is given as paramter, use this one, otherwise search one
# [-1] -> no new cycle detected
def get_new_path(g,start=-1):
   if start == -1:
      start = find_first_edge(g)
      if start == [-1]:
         return [-1]

   new_path = [start]
   next_node = get_next_node_delete_edge(g,new_path[-1])
   while(next_node != -1):
      new_path += [next_node]
      next_node = get_next_node_delete_edge(g,new_path[-1])
   return new_path

def find_eulerian_path(adj_matrix,start_node):
   # copy adjacency matrix - will be destroyed, since edges will be removed
   g = [end[:] for end in adj_matrix]

   # step 1: create longest possible path, start and end in node with odd node degrees
   complete_path = get_new_path(g,start_node)

   # step 2: find cycles and integrate them into complete_path 
   new_cycle = get_new_path(g)
   while new_cycle[0] != -1:
      #integrate new cycle into the existing one
      i = complete_path.index(new_cycle[0])
      complete_path = complete_path[:i] + new_cycle + complete_path[i+1:]
      new_cycle = get_new_path(g)
   return complete_path

start_node = initial_checks_ok(g)
if start_node != -1:
   print(find_eulerian_path(g,start_node))


