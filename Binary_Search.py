list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
list_1.sort()

#Binary Search
list_1.sort()
list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
def bin_search(list_1, target):
  '''
  Searches for a target value in a given SORTED  list, if the value DNE in the list returns -1 
  param: list, int
  return: index target or -1 
  '''
  start = 0 
  end = len(list_1)

  while True: 
    if list_1[(start+end)//2] == target:
      return ((start+end)//2)
    elif start+1 == end:
      return -1
    elif list_1[(start+end)//2] > target:
      
      end = (start+end)//2 
    else:
      start = (start+end)//2

