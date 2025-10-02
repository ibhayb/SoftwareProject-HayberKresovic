# breadth-first search
#
# Software for educational purposes only. No warranty of any kind.
#
# Author: Jens Liebehenschel
# Copyright 2024

import math
inf = math.inf

# coloring of nodes
WHITE = 1
GRAY = 2
BLACK = 3

# to be counted up to fill enter_time and leave_time
time = 0

# n x n adjacency matrix
n = 0

# arrays as global variables
color = []
predecessor = []
distance = []
enter_time = []
leave_time = []

# Queue to be used by bfs
# enqueue: append
# enqueue: pop(0) 
q = []

# to be called before calling bfs_all
def initialization(graph):
   global time, n, color, predecessor, distance, enter_time, leave_time

   # time counted up to fill enter_time and leave_time
   time = 0

   # n x n adjacency matrix
   n = len(graph)

   # allocate arrays for keeping information
   # coloring of nodes
   color = [inf]*n
   # predecessor of discovered node
   predecessor = [inf]*n
   # distance to starting node in (sub-)graph
   distance = [inf]*n
   # order of visiting the nodes
   enter_time = [inf]*n
   leave_time = [inf]*n

   # initialize arrays
   for i in range(n):
      color[i] = WHITE
      predecessor[i] = -1
      distance[i] = inf
      enter_time[i] = -1
      leave_time[i] = -1

# perform breadth-first search until all nodes are discovered
# several new starting nodes are selected if necessary
def bfs_all(graph):
   global time, q
   for node in range(n):
      if color[node] == WHITE:
         time += 1
         enter_time[node] = time
         color[node] = GRAY
         distance[node] = 0
         predecessor[node] = 0
         q = [node]
         bfs(graph)

# perform breadth-first search with start node in queue
def bfs(graph):
   global time, q
   while len(q) > 0:
      node = q.pop(0)
      # search for adjacent and unvisited nodes
      for succ in range(n):
         if graph[node][succ] > 0 and color[succ] == WHITE:
            time += 1
            enter_time[succ] = time
            color[succ] = GRAY
            predecessor[succ] = node + 1 # + 1 due to numbering scheme
            distance[succ] = distance[node] + graph[node][succ]
            q.append(succ)
      color[node] = BLACK
      time += 1
      leave_time[node] = time


