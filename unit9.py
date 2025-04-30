 # time complexity 
# what is the time complexity of mystrey_function()? you may assume root refers to the root node of a balanced binary search tree

class TreeNode:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right
    
    def mystrey_function(root,key):
        # if the root is None, return None
        if root is None:
            return TreeNode(key,value)
        # if the key is equal to the value of the root node, return the root node
   
        if key < root.val:
            root.left = mystrey_function(root.left, key, value)
        elif key > root.val:
            root.right = mystrey_function(root.right, key, value)
        else:
            root.val = value
        return root
    


# draw a tree with root root 
class TreeNode:
    def __init__(self,value=0, left=None, right=None):
           
        self.val = value
        self.left = left
        self.right = right
        
root = TreeNode()
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(6)
root.left.right = TreeNode(7)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
    #    0
    #    / \
    #   2   3
    #  / \  / \
    # 6   7 4  5

class TreeNode:
    def __init__(self,value=0, left=None, right=None):
           
        self.val = value
        self.left = left
        self.right = right
def mystrey_function(node):
    if node is None:
        return 0
    # calculate the sum of the left and right subtrees
    left_sum = mystrey_function(node.left)
    right_sum = mystrey_function(node.right)
    # return the sum of the current node's value and the sums of its left and right subtrees
    return 1 + max(left_sum, right_sum)
  
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

output = mystrey_function(root)
print(output)  # Output: 3 (the longest path is from node 4 to node 5 through node 2)


# the following function level_order() imtends to return a list of node values traversed in level order. however, the function level_order() has abug! which of the following options fixes the bug?
from collections import deque
class  TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def level_order(root):
    if not root :
        return 
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

output = level_order(root)
print(output)  # Output: [1, 2, 3, 4, 5]


 # given the root of abinary tree where each node has integer values, return the 
 # sum of all left leaves. a leaf is a node with no children. a left leaf is a leaf 
 # thar is the left child of anither node. as such, a tree with only one node has no left leaves


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    if not root:
        return 0

    # Check if the left child is a leaf
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_of_left_leaves(root.right)
    
    # Recur for left and right subtrees
    return sum_of_left_leaves(root.left) + sum_of_left_leaves(root.right)

# Example Tree:
#         3
#        / \
#       9   20
#           / \
#          15  7

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

output = sum_of_left_leaves(root)
print(output)  # Output: 24 (9 + 15)


