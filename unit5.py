# 

# write a fun that adds each elemet values as a node with values [i] to the linked list
class Node:
    
        def __init__(self, value, next_node=None):
               self.value = value
               self.next = next_node
def extend_linked_list(tail, values):
        
        for i in values:
            tail.next = Node(i)
            tail = tail.next
        return tail
   
# Problem 1: Detect Circular Linked List
# A circular linked list is a linked list where the tail node points at the head node. Given the head of a linked list, write a function is_circular() that returns True if the linked list is circular and False otherwise.

# Note: a circular list is more than just a cycle - specifically connecting the first and last nodes.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_circular(head):
    current = head
    while current.next:
        current = current.next
        if current.next == head:
            return True
       
    return False


num1 = Node(1)
num2 = Node(2)
num3 = Node(3)
num1.next = num2
num2.next = num3
num3.next = num1
# num1 -> num2 -> num3 -> num1
print(is_circular(num1))


var1 = Node(4)
var2 = Node(5)
var3 = Node(6)
var1.next = var2
var2.next = var3
var3.next = None
# var1 -> var2 -> var3
print(is_circular(var1))

#pointer that will keep checking if the next node is head
#if the next node is head then it will return true
#return false otherwise
#we will also update node every time
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def is_circular(head):
    current = head
    while current.next:
        current = current.next
        if current.next == head:
              return True
    return False
# num1 -> num2 -> num3 -> num1
# num1 = Node("num1")
# num2 = Node("num2", num1)
# num3 = Node("num3", num2)
num3 = Node("num3")
num2 = Node("num2", num3)
num1 = Node("num1", num2)
num1.next = num2
num2.next = num3
num3.next = num1
print(is_circular(num1))
# var1 -> var2 -> var3
# print(is_circular(var1))
var1 = Node(10)
var2 = Node(20)
var3 = Node(30)
var1.next = var2
var2.next = var3
var3.next = None  # No cycle
# var1 -> var2 -> var3
print(is_circular(var1))