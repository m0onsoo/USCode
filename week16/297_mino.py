# Given
# serialization - a binary tree
# deserialization - a string

# Goal
# serialize / deserialize a binary tree

# Input / output
# serialize - a binary tree / string
# deserialize - string / binary tree

# Example
# [1,2,null] -> 1/2/null
# [1,null,2] -> 1/null/2
# [1,2,3,null,null,4,5] -> "1/2/3/null/null/4/5"
# [1,2,3,null,4,null,null] -> "1/2/3/null/4/null/null"

# Approach
# serialization step:
# traverse nodes at depth level
# append each node value to the string including null
# add a new node with a slash to distinguish

def serialize(self, rooot:Optional[TreeNode]) -> str:
  curr_nodes = []
  next_nodes = [root]
  isValid = True
  serialized = ""
  
  
  while next_nodes and isValid:
    curr_nodes, next_nodes = next_nodes, []
    
    isValid = False
    for node in curr_nodes:
      if node:
        serialized += node.val+'/'
        isValid = True
      else:
        serialized += "null"+'/'
        
      if node:
        next_nodes.append(node.left)
        next_nodes.append(node.right)
      else:
        next_nodes.append(None)
        next_nodes.append(None)
        
    return serialized