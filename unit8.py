class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode('a')
x = TreeNode('x')
y = TreeNode('y')
e = TreeNode('e')
m = TreeNode('m')
p = TreeNode('p')

a.left = x
a. right = y

x.left = e
x.right = m

y.right = p

root = a  # reference to the root node of the tree(a)

# which of the following best represents the values of the tree with root root

#          root
#          /   \
#        a
#        x       y
#       / \       \
#      e   m       p

#  Correct Answer:
    #        a
    #      /   \
    #     /     \
    #    x       y
    #   / \       \
    #  e   m       p

# the following function find() should take in the root of a binary tree and a value target and return true if there is a node with value target in the tree and false otherwise. however, it has a bug

# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def find(root, target):
#     if not root:
#         return False
#     if root.val == target:
#         return True
#     return find(root.left, target) and  find(root.right, target)

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def mystery_function(root):
    if not root:
        return 0
    return 1 + mystery_function(root.left) + mystery_function(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

output = mystery_function(root)
# print(output)  # Output: 4, as there are 4 nodes in the tree ?redi

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def insert_node(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_tree(root):
    if not root:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)


# given the root of a binary search tree, remove the node with the value val into the tree. all nodes in the tree are guaranteed to be unique. return the root.
#  if you need to replace a parent node with two childeren , use the in_order successor of that node, such that replacement.val is the smallest value greater than removed.val

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def remove_node(root, val):
    if not root:
        return None
    if val < root.val:
        root.left = remove_node(root.left, val)
    elif val > root.val:
        root.right = remove_node(root.right, val)
    else:
        # Node to be deleted found
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # Find the in-order successor (smallest node in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            # Replace the current node's value with the successor's value
            root.val = successor.val
            # Remove the successor node from the right subtree
            root.right = remove_node(root.right, successor.val)
    return root


root = TreeNode(5)
root = insert_node(root, 3)
root = insert_node(root, 7)
root = insert_node(root, 2)
root = insert_node(root, 4)
root = insert_node(root, 6)
root = insert_node(root, 8)

root = remove_node(root, 7) 





def remove_node(root, value):
    # Write your code here

    if not root:
        return None
    if value < root.val:
        root.left = remove_node(root.left, value)
    elif value > root.val:
        root.right = remove_node(root.right, value)
    else:
      
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
    
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = remove_node(root.right, successor.val)
    return root