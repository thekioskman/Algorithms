#Sorting algorithms: Bubble, Selection, Insertion, Merge 


#Bubble sort
list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
def bubble_sort(list_1):
  '''
  Sorts a given list 
  param: list 
  return: list 
  '''
  for i in range(len(list_1)):
    for j in range(len(list_1)-1):
      if list_1[j] > list_1[j+1]:
        temp = list_1[j]
        list_1[j] = list_1[j+1]
        list_1[j+1] = temp
  return list_1

#Insertion Sort 
list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
def insertio_sort(list_1):
  '''
  Sorts a given list 
  peram: list 
  return: list 
  '''
  for i in range(len(list_1)):
    j = i #saves value of i
    while list_1[j] < list_1[j-1] and j > 0:
      temp = list_1[j-1]
      list_1[j-1] = list_1[j]
      list_1[j] = temp
      j -= 1 
  return list_1

#Selection Sort 
list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
def selectio_sort(list_1):
  '''
  Sorts a given list
  param: list
  return: list 
  '''
  return_list = []
  for loops in range(len(list_1)):
    return_list.append(min(list_1))
    list_1.remove(min(list_1))
  return return_list
#Merge Sort 
def merge(right_list, left_list):
  '''
  Combines two lists in sorted order 
  param: list
  return: list 
  '''
  return_list = []
  while right_list and left_list:
    if right_list[0] < left_list[0]:
      temp = right_list.pop(0)
      return_list.append(temp)
    else:
      temp = left_list.pop(0)
      return_list.append(temp)
  if not(right_list):
    return_list += left_list
  else:
    return_list += right_list
  return return_list

list_1 = [1,23,32,4523,4,2345,23,4213,4,143]
def merge_sort(list_1):
  '''
  Sorts a given list 
  param: list
  return: list 
  '''
  if len(list_1) <= 1:
    return list_1 
  else:
    right_list = []
    left_list = []
    for i in range(len(list_1)):
      if i < len(list_1)//2:
        left_list.append(list_1[i])
      else:
        right_list.append(list_1[i])
  
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(right_list, left_list)  

print(merge_sort(list_1))
print(list_1)
