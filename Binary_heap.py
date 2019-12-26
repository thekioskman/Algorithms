#A heap is a tree based data stucture, it is a way to store data 

#The number of children any given parent node can have depends on the type of heap
#Most commonly they only have two children, this is known as a binary heap 

#Heaps have many applications, such as heapsort or priority queue 

#In a heap, every level should be completely filled except for the last level, in other words, its a complete tree 

#There a min heaps and max heaps, either the max value is at the top, or the min value is at the top 

#The children on any given level have no relation to eachother, the only constant we can derive from a heap is that either the high priority target(max) is at the root of the lower priority target(min) is at the heap 



#heap repersentation is an array
#We skip the zero index and start from index 1
#Left child: 2*i
#Right child: 2*i +1
#Parent: i//2  
heap = [None]


def insert(element):
  '''
  Inserts and element into the heap 
  param: int 
  return: None 
  '''
  index = len(heap)
  heap.append(element)
  while index//2 > 0:
    if heap[index//2] > element:
      temp = heap[index//2]
      heap[index//2] = element
      heap[index] = temp
    index //= 2

def min_child(index):
  '''
  Return the index of the minumin child of the parent index 
  param: int 
  return: int
  '''
  if index *2 +1 > len(heap)-1:
    return index*2
  else:
    if heap[index*2] < heap[index*2+1]:
      #compare left child and right child 
      return index*2
    else:
      return index*2+1
  

def get_min():
  '''
  Return the minimum element in the heap 
  param: none 
  return: 
  '''
  #Save min value 
  min_val = heap[1]
  #Replace min value with last value 
  heap[1] = heap[-1]
  #Remove last value 
  heap.pop(-1)
  
  index = 1 
  
  while index*2 < len(heap)-1:
    mc = min_child(index)
    if heap[index] > heap[mc]:
      temp = heap[mc]
      heap[mc] = heap[index]
      heap[index] = temp
    index = mc 
  
  return min_val 





    
  
