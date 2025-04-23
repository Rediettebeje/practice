class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def collect_values(node):
    if not node:
        return []
    return [node.val] + collect_values(node.left) + collect_values(node.right)

root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

all_values = collect_values(root)
print(all_values)

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if root.val == root.left.val + root.right.val:
        return True
    else:
        return False


# Create the tree
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

root.val = 10
root.left.val = 3
root.right.val = 5


# Check the condition
result = check_tree(root)
print(result)  # Output: True



class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False
    left_val = right_val = 0

    if root.left:
        left_val = root.left.val
    if root.right:
        right_val = root.right.val
    summ= right_val + left_val
    return  root.val == summ


# Given the root of a binary tree, write a function height() that 
# returns the height of a binary tree.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def height(root):

    if not root:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    if lheight > rheight:
        return lheight + 1
    return rheight + 1

print(height(root))





    
    
    