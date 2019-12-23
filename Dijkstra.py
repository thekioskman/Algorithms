from math import inf 
#Find the shortest path from point A - B 
#First implementation without priority Queue 
graph = {}
graph[1] = [(1,4),(2,5),(3,6),(4,0)]
graph[2] = [(1,6),(2,20),(3,100)]
graph[3] = [(5,56)]
graph[4] = [(5,67)]
graph[5] = [(1,5),(2,3),(3,9)]

def djk(graph,start):
  '''
  Find the shortes path from A to all other nodes 
  param: dic
  return: None
  '''
  #Initialize 
  visited = [False] * (len(graph)+1)
  distance = [inf] * (len(graph)+1)
  visited[start] = True 
  distance[start] = 0
  curr_node = start
  #Runs it for each Vertex in the graph  
  for loops in range(len(graph)):
    #Update distances 
    for adj_node in graph[curr_node]:
      if not(visited[adj_node[0]]):
        if adj_node[1] + distance[curr_node] < distance[adj_node[0]]:
          distance[adj_node[0]] = adj_node[1] + distance[curr_node]
    
    #Determine next curr_node
    temp_min = inf
    for node in range(1,6):
      if not(visited[node]):
        if distance[node] < temp_min:
          temp_min = distance[node]
          curr_node = node
    
    #As a failsafe
    if temp_min == inf:
      break
    else:
      visited[curr_node] = True 
    


  print(distance[1:])

djk(graph,1)
