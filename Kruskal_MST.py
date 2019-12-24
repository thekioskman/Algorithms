#Kruskal Algorithm
graph2 = {}
graph2[1] = [(1,4),(2,5),(3,7),(4,0)]
graph2[2] = [(1,6),(2,20),(3,100)]
graph2[3] = [(5,56),(6,7)]
graph2[4] = [(7,11),(5,67)]
graph2[5] = [(1,5),(2,56),(3,9)]
graph2[6] = [(1,20), (4,10)]
graph2[7] = [(4,1000)]



#Find parent node of a set 
def parent_node(node):
  '''
  find which set the node belongs to
  param: int
  return: int
  '''
  if parent[node] == node:
    return node 
  else:
    return parent_node(parent[node])

#Union two sets
def union(node1, node2):
  '''
  merges two sets of nodes together
  param: int, int
  return: None 
  '''
  parent[parent_node(node1)] = node2

#Every node starts of as its own parent, meaning it is in a set by itself 
parent = {x:x for x in range(1,len(graph2)+1)}

def kruskal(graph):
  '''
  Runs kruskal MST on a graph 
  param: dict 
  return: dict 
  '''
  return_graph = {x:[] for x in range(1,len(graph)+1)}


  #Sort edges by weight value 
  edges = []
  for key in graph:
    for edge in graph[key]:
      edges.append((key,edge[0],edge[1]))
  
  #This sorts it by the second tuple value, or the weight of the edge 
  edges = sorted(edges, key = lambda x : x[2])

  #Go through the sorted edges and add them if they do not create a cycle
  for edge in edges:
    if parent_node(edge[0]) != parent_node(edge[1]):
      union(edge[0],edge[1])
      return_graph[edge[0]].append((edge[1] , edge[2]))
      return_graph[edge[1]].append((edge[0] , edge[2]))
    else:
      continue 

  return return_graph

print(kruskal(graph2))
