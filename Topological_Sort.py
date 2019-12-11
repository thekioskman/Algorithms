#Topological Sort 
#initialize graph, nodes and connections
num_nodes = 5
graph = {}

for x in range(num_nodes):
  graph[x] = []
graph[0] = [1]
graph[1] = [4]
graph[2] = [1,3]
graph[3] = [1,4]
graph[4] = [0]

def topo(graph):
  '''
  Run topological sort on the graph, returns edges that are not part of a loop in order of dependance  
  '''
  #Initialization of edge list visited list and q 
  
  return_list = []
  num_edges = [0]*len(graph)
  for adj_node in graph.keys():
    for node in graph[adj_node]:
      num_edges[node] += 1 

  q = []
  visited = [False] * len(graph)

  #Check if there is a vertex with no dependance

  for node in range(len(num_edges)):
    if num_edges[node] == 0:
      q.append(node)
      visited[node] = True 
  
  while q:
    
    curr_node = q.pop(0)
    return_list.append(curr_node)
    visited[curr_node] = True 
    
    #Update num_edges list
    
    for adj_node in graph[curr_node]:
      num_edges[adj_node] -= 1
    
    #procces new nodes 

    for node in range(len(num_edges)):
      if num_edges[node] == 0:
        if not(visited[node]):
          q.append(node) 

  return return_list

print(topo(graph))
#Since 2 and 3 are returned in means there is a loop with nodes 0,1 and 4 
