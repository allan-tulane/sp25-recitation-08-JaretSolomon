from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
  pq = [(0, 0, source)] 
  visited = {}

  while pq:
      weight, edges, node = heappop(pq)
      if node in visited:
          previous_weight, previous_edges = visited[node]
          if weight > previous_weight or (weight == previous_weight and edges >= previous_edges):
              continue

      visited[node] = (weight, edges)

      for neighbor, w in graph.get(node, []):
          new_weight = weight + w
          n_edges = edges + 1
          heappush(pq, (new_weight, n_edges, neighbor))

  return visited
    
    


def bfs_path(graph, source):
  parents = {source: None}
  queue = deque([source])
  while queue:
      current = queue.popleft()
      for neighbors in graph.get(curr, []):
          if neighbors not in parents:
              parents[neighbors] = curr
              queue.append(neighbors)

  return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
  path = []
  curr = destination
  while current is not None:
      path.append(curr)
      current = parents.get(curr)
  path.reverse()
  return ''.join(path[:-1])