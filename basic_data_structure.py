#Basic Data Structure 
"""
-- Array -> list 
-- Queue(FIFO) -> list, insert(0, val), pop()
-- Stack (LIFO) -> list, append(), pop() 
-- Dequeue -> import collections from deque, append() , appendleft(), pop(), popleft()
-- linked list -> object (important). Node => self.val, self.next 
-- Hash table -> dictionary (important)
-- Binary Tree -> Node=> self.left, self.right, self.data 
-- Binary Search Tree -> leftsubtree(keys) < node(key)<rightsubtree(keys)
-- Heap -> max Heap => subNode(keys) < node(key), Min Heal => subNode(keys) > node(key) 
"""
#Linked list 
"""
when chaning a link list, the only thing need to change is the pointer 
"""
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self,nextval = None

class LinkedList: 
    def __init__(self):
        self.headval = None               


#Stack LIFO
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peak(self):
        return self.items[len(self.items)-1]

#Queue FIFO
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self, item):
        return self.items.pop()


#deque 
from collections import Counter, deque
d = deque("apple")
d.append('s')
d.appendleft('a')
d.pop()
d.popleft()

def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)

#Hash -> dictionary  
for key, val in graph_elements.items():
    print(key , '->', val)

graph_elements.keys()
graph_elements.values()

#Binary Tree
class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftnode = None
        self.rightnode = None 

    def insert_left(self, Node):
        if self.leftnode == None:
            self.leftnode = BinaryTree(Node)
        else: 
            #if the node already has a left node, then push the existing node to next level 
            leaf = BinaryTree(Node)
            self.leftnode, leaf.leftnode = leaf, self.leftnode
    def insert_right (self, Node):
        if self.rightnode == None: 
            self.rightnode = BinaryTree(Node)
        else:
            leaf = BinaryTree(Node)
            self.rightnode, leaf.leftnode = leaf , self.rightnode
    def get_root_val(self):
        return self.key
    def ser_root_val(self, val):
        self.key = val
    def get_left_child(self):
        return self.leftnode
    def get_right_child(self):
        return self.rightnode


preorder => root, left, right
inorder => left, root, right  
postorder => left, right, root 
 
"""
traversals 
preorder: root-> left -> right 
inorder: left -> root -> right 
postorder: left-> right -> root 
"""
def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree is not None: 
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree is not None: 
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())
        
#Binary Search Tree 
"""
node.left.val<node.data.val<node.right.val
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None 

    def insert(self,node):
        if self.root is None:
            self.root = node 
        else:
            if node.val < self.root.val:
                if self.root.left_child is None:
                    self.root.left_child = node 
                else insert()  #TODO 
 

#Heap 
"""
Binary Heap 
MAX HEAP => node.data.val > node.left.val AND node.data.val > node.right.val 
MIN HEAP => node.data.val < node.left.val AND node.data.val < node.right.val 

root (len-1)/2
left child len*2+1 
right child len*2 +2 

"""
#heaplify => build a heap  

class BinaryHeap:
    def _init__(self, root):
        #start with a index 0 for 0 
        self.heap_list = []

    def insert(self, val):
        self.heap_list.append(val)
        self.swap_up(len(self.heap_list)) 

    def swap_up(self, position):
        #no return value for this funciton, because we are changing the array
        while position // 2 > 0:
            if self.heap_list[position] < self.heap_list[(position-1)//2]:
                #sawp 
                self.heap_list[(position-1)//2], self.heap_list[position] = self.heap_list[position],self.heap_list[(position-1)//2]
            position = (position -1)//2



#Graphs 
graph_elements = { "a" : ["b","c"],
                    "b" : ["a", "d"],
                    "c" : ["a", "d"],
                    "d" : ["e"],
                    "e" : ["d"]
                    }

