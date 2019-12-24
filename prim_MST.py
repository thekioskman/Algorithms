from math import inf 
#Prim Algorithm 
graph = {}
graph[1] = [(1,4),(2,5),(3,7),(4,0)]
graph[2] = [(1,6),(2,20),(3,100)]
graph[3] = [(5,56)]
graph[4] = [(5,67)]
graph[5] = [(1,5),(2,56),(3,9)]

def prim(graph, start):
  '''
  Runs prims algorithm on a weighted graph from any given starting node 
  param: dict , int
  return: none 
  '''
  visited = [False] * (len(graph)+1)
  distance = [inf] * (len(graph)+1)
  parent = [-1] * (len(graph)+1)
  visited[start] = True 
  distance[start] = 0
  curr_node = start
  #For a MST we will always have E = V-1 
  for loops in range(len(graph)-1):
    #Update all paths that stem from the current node 
    #Update the parent of the curr_node:
    for adj_node in graph[curr_node]:
      if not(visited[adj_node[0]]):
        if adj_node[1] < distance[adj_node[0]]:
          distance[adj_node[0]] = adj_node[1]
          parent[adj_node[0]] = curr_node


    #Pick the next current node and update the visited array 
    temp_list = []
    #pick the path from our current node that has the lowest weight
    for node in range(len(distance)):
      if visited[node]:
        temp_list.append(inf)
      else:
        temp_list.append(distance[node])
    #pick min distance
    curr_node = temp_list.index(min(temp_list))
    #update visted
    visited[curr_node] = True
  
  #The distances at index 0 are non inf because the first vertex is at point 1
  print(distance)
  print(parent)

prim(graph,1)
