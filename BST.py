#Creating a tree and implementing binary search using the tree 
class Node:
  def __init__(self, value):
    self.value = value 
    self.left_child = None
    self.right_child = None  


  def __str__(self):
    return str(self.value)
  
  def set_left(self, left_val):
    self.left_child = Node(left_val)
 
  def set_right(self, right_val):
    self.right_child = Node(right_val)  
   

class BST:
  def __init__(self, value=None):
    self.root = Node(value)

  def find_min(self, node):
    if node.left_child:
      return self.find_min(node.left_child)
    else:
      temp = node.value 
      node = None 
      return temp
  def call_search(self, target):
    curr_node = self.root
    return self.search(target, curr_node)
  
  def call_insert(self, target):
    curr_node = self.root
    return self.insert(target, curr_node)
  
  def call_delete(self, target):
    curr_node = self.root
    return self.delete(target, curr_node)
  
  def search(self, target, curr_node):
    if curr_node is None:
      return False 
    elif target == curr_node.value:
      return True  
    elif curr_node.right_child == None and curr_node.left_child == None:
      return False   
    elif target > curr_node.value:
      return self.search(target, curr_node.right_child )
    else:
      return self.search(target, curr_node.left_child )

  def insert(self, value, curr_node):
    if curr_node is None:
      curr_node.value = value  
    else:
      if value < curr_node.value:
        if curr_node.left_child is None:
          curr_node.set_left(value)
        else:
          return self.insert( value, curr_node.left_child)  
      else:
        if curr_node.right_child is None:
          curr_node.set_right(value)
        else:
          return self.insert( value, curr_node.right_child) 

  def delete(self, value, curr_node):
    if curr_node is None:
      return "Node does not exist"
    
    if value == curr_node.value:
      if curr_node.right_child and curr_node.left_child:
        curr_node.value = self.find_min(curr_node.right_child)

      elif curr_node.right_child:
        curr_node = curr_node.right_child
        curr_node.right_child = None  
      elif curr_node.left_child:
        curr_node = curr_node.left_child
        curr_node.left_child = None 
     
    elif value > curr_node.value:
      self.delete(value, curr_node.right_child)
    else:
      self.delete(value, curr_node.left_child)
  def call_in_order(self):
    curr_node = self.root
    return self.in_order(curr_node)
  
  def in_order(self, curr_node, return_list = []):
    if curr_node is None:
      return return_list
    else:
      return in_order(curr_node.left_child) +[curr_node] + in_order(curr_node.right_child)
  def call_post_order(self):
    curr_node = self.root
    return self.post_order(curr_node)
    
  def post_order(self, curr_node)

       

test = BST(6)
test.call_insert(9)
test.call_insert(8)
test.call_insert(15)
test.call_insert(2)
test.call_insert(1)
test.call_insert(13)
test.call_insert(11)
test.call_insert(18)
test.call_delete(9)
print(test.call_search(9))
print(test.call_search(18))
