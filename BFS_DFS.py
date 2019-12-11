#BFS and DFS
from math import inf
#sample graph 
num_nodes = 5
graph = {}
#Unweighted Graph 
for x in range(num_nodes):
  graph[x] = []
graph[0] = [1,4]
graph[1] = [0,4,3]
graph[2] = [1,3]
graph[3] = [1,2,4]
graph[4] = [0,1,3]


#BFS
#initialization of BFS
def bread_search(start,graph):  
  dist = [inf] *len(graph)
  q = []
  visited = [False] * len(graph)

  q.append(start)
  visited[start] = True 
  dist[start] = 0
  counter = 0
  while q:

    curr_node = q.pop(0)
    print(curr_node)
    #Procces the current node that we are one with respect to the goal of the program , lets say we want to find the greatest distance 
    if graph[curr_node]:
      counter += 1


    for adj_node in graph[curr_node]:
      if not(visited[adj_node]):
        q.append(adj_node)
        visited[adj_node] = True 
      if dist[adj_node] == inf:
        dist[adj_node] = counter 
  return dist

print(bread_search(0,graph))
    

#DFS 
#Take the same sample graph 

def deep_search(start, graph):
  q = []
  dist = [inf] * len(graph)
  visited = [False] * len(graph)
  counter = 0

  dist[start] = 0
  visited[start] = True 

  q.append(start)
  while q:
    curr_node = q.pop(-1)
    print(curr_node)
    
   
    for adj_node in graph[curr_node]:
      if not(visited[adj_node]):
        q.append(adj_node)
        visited[adj_node] = True 

deep_search(0,graph)

