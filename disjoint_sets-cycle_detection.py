#Disjoint set tree implementation 
#Disjoints sets are used in kruskall graphing algorithm 
#Support two operations, find and union 
#All data point should be distinct 


#initially all elements are in thier own groups, we distinguish groups using a parent, that is how items are identified. If two elements have the same parent they are in the same group 

data = [1,2,3,4,5,6,7,8,9]

#every elements starts off being its own parent, therefore the index of the parent is -1, the parent array will give the index of the parent. Therfore, parent[i] will return the parent of the i'th value from the data array  
parent = [-1] * 9


def find1(index):
  '''
  find the parent of an element 
  param: index of the element 
  return: the index of the parent of the elemenet 
  '''
  global data, parent
  
  if parent[index] == -1:
    return data[index]
  else:
    return find1(parent[index])

def union1(val1, val2):
  '''
  Unions two values that are from different sets 
  param: element 
  return: None 
  '''
  global data, parent 
  
  parent[data.index(find1(data.index(val1)))] = data.index(val2) 

union1(1,2)
union1(2,3)
union1(1,7)
union1(9,7)

print(find1(data.index(9)))
print(find1(data.index(2)))
print(find1(data.index(3)))
print(find1(data.index(1)))

#Dictionary repersentation 


#Each element which exists as a key, will be mapped to a parent so we can just find the parent by calling the dic[element], therefore we can just have the elements themselves repersent the parents as opposed to having the parents be repersent by indexes 

parent2 = {x:x for x in range(1,10)}

def find(element):
  '''
  returns the repersenative of the set 
  param: elements
  return: the value of the parent
  '''
  if parent2[element] == element:
    return element 
  else:
    return find(parent2[element]) 

def union(element, element2):
  '''
  unions two sets 
  param: elements 
  return: None 
  '''
  parent2[find(element)] = element2 

union(1,2)
union(2,3)
union(1,7)


union(4,9)
union(5,4)
union(5,6)
print(find(4))
print(find(5))
print(find(9))
print(find(1))
  

#Disjoin sets have application in cycle detection 

#Cycle detection in an unweight graph using disjoint sets 
#For this representation we will use a dictionary to track our sets 

#Our temp Graph 
graph = {}
graph[1] = [2,3]
graph[2] = [3,4]
graph[3] = [1,2]
graph[4] = [2]


sets = {x:x for x in range(1,len(graph)+1)}

def root_node(node):
  '''
  Returns the parent of the a node
  param: int 
  return: int 
  '''
  if sets[node] == node:
    return node
  else:
    return root_node(sets[node])


def set_union(node1, node2):
  '''
  Unions two nodes together that are connected by an egde 
  param: int, int
  return: None 
  '''
  sets[root_node(node1)] = node2


def iscycle(graph):
  '''
  Checks if there is a cycle in the graph
  param: dict
  reutnr None 
  '''
  for node in graph:
    for adj_node in graph[node]:
      if root_node(node) == root_node(adj_node):
        return True
      else:
        set_union(node,adj_node)

print(iscycle(graph))

