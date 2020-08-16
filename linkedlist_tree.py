# 1. transpose of a matrix
matrix = [[1,2,3,4],[4,5,6,7]]
transp_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0])) ]

#1.1 Tower of Hanoi
def Move(fromPol, toPol):
    print("Moving disk from ", fromPol, toPol)

def Tower(num, fromPol, toPol, sparePol):
    if num ==1:
        Move(fromPol,toPol)
    else:
        Tower(num-1,fromPol,sparePol,toPol)
        Tower(1,fromPol,toPol,sparePol)
        Tower(num-1,sparePol,toPol,fromPol)


#2. Fibonacci
from typing import List, Dict, Tuple, Set
def fib(x:int)->int:
    if x < 0:
        raise("negative value ")
    elif x<=1:
        return x
    else:
        return(fib(x-1)+fib(x-2))
    
[fib(x) for x in range(10)]

#dynamic programming 
def fib_dp(x:int)->int:
    mome = [None]*(x+1) #1 larger than number 
    if mome[x] is not None:
        return mome[x]
    if x <0:
        raise("Negative value is not accpetible")
    elif x==1 or x ==2:
        result = 1 
    else:
        result = fib_dp(x-1)+fib_dp(x-2)
    mome[x] = result 
    return result 

def fib_bottom_up(x:int)->int:
    if x==1 or x==2:
        result = 1 
    else:
        mome = [0]+[None]*(x)

        mome[1], mome[2] = 1 , 1  
        for i in range(3, n+1):
            mome[x] = mome(x-1)+mome(x-2)
        result = mome[x]
    return result  

def fib1():
    a, b = 0,1
    while True:
        yield a 
        a , b = b, a+b 

#2.2 longest common subsequence 
"""
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
The key point for this solution is to use hash table to remember the index of each character
"""
def lengthOfLongestSubstring(s:str)->int:
    if not s:
        return 0
    #start to remember the current non-repeatible substring start point 
    #max_len to record the current max len 
    #h_map to remember the newest index of each character  
    start, max_len, h_map = 0,0,{}
    for i, char in enumerate(s):
        #when finding a match, check if starting anchor is less than the duplicated index 
        if char in h_map and start<=h_map[char]:
            start = h_map[char]+1 #move the starting anchor to            
        else: 
            max_len = max(max_len, i-start+1) 
        h_map[char]=i
    return max_len


#2.3 knapsack   


#3. if Reversed 
def isReserse(s:str, w:str)-> bool:
    if len(s) != len(w):
        return False
    else:
        for i, char in enumerate(s):
            if char != w[len(w)-(i+1)]:
                return False
            else:
                return True 

#4. merge two linked list 
class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: 
            return None 
        
        node = ListNode() #node to traverse throught the linked list 
        merged = node #merge as the anchor to the return linkedlist 
        
        if l1.val<=l2.val:
            #linked smaller node to merged list 
            node.next=l1
            #move link point to l1 next node object 
            l1 = l1.next 
        else:
            node.next, l2 = l2, l2.next 

        #when finish looping one of the linked list     
        if not l1 or l2:
            node.next =  l1.next or l2.next 
        
        #node has become a pointer of last item of l1 and l2, 
        #so return the reserved merged node to print the entire linked list 
        return merged.next 
 
#Prtition list 
"""
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
The most important tips are: 1, one node anchor as the begining (head) 2. one node to traverse
"""
class Solution:


        #when traversing linkedin list, always preserve the original list 
        #and use a node to traverse the linked list 
        left_node = ListNode()
        right_node = ListNode()
        node_l, node_r = left_node, right_node  
        
        while head is not None:
            if head.val < x:
                node_l.next = head  #add to node 
                node_l = node_l.next  #move node to next one 
            else:
                node_r.next = head 
                node_r = node_r.next

            head = head.next #move the original list curser 
        
        node_l.next = right_node.next #linked the left list last node to right list first node 
        node_r.next = None 
        
        return left_node.next

#160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    curA ,curB = headA, headB
    
    len_A = self.lenof(curA)
    len_B = self.lenof(curB)
    
    if (len_A>len_B):
        for _ in range(len_A-len_B):
            headA = headA.next
    elif (len_B>len_A):
        for _ in range(len_B-len_A):
            headB = headB.next
    else:
        while headA != headB:
            headA = headA.next
            headB = headB.next
    return headA

def lenof(self,llist):
    count = 0 
    while llist:
        llist = llist.next
        count+=1

#203. Remove Linked List Elements
"""
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
def removeElements(self, head: ListNode, val: int) -> ListNode:
    #we need to preserve the current node and only checking the next value 
    #so we need to make sure the first value is not in the target 
    while head and head.val == val:
        head = head.next 
    
    #remember to keep head anchor and use a seperate node to traverse the linked list 
    #remember to use == as eual 
    node = head 
    while node:
        if node.next and node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next 
    return head 

#206. Reverse Linked List
"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""        
def reverseList(self, head: ListNode) -> ListNode:
    pre = None #setting up a previouse anchor 
    next_link = None #setting up next link anchor 
    node = head 

    while node:
        next_node= node.next #need to preserve the link to next node 
        node.next = pre
        pre = node 
        node = next_node 
    return pre

#2. Add Two Numbers
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    sum_list= ListNode()
    temp = sum_list #an temp mode to establish link to others 
    sum_val, pass_val = 0,0 

    #check num for the case [5]+[5] =[0][1]
    while l1 and l2 and pass_val:
        sum_val = pass_val
        if l1: #for uneven l1 and l2
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        new_node = ListNode(sum_val%10)
        temp.next = new_node
        pass_val = sum_val//10
        temp = temp.next

    return sum_list.next


#Tree 
"""
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
recursively calling matdepth with incremental 
"""
class TreeNode:
    def __init__(self, val =0, left=None, right=None):
        self.val = 0
        self.left = left
        self.right = right 

def maxdepth(root:TreeNode)->int:
    if root is None:
        return 0 
    else:
        left_height = maxdepth(root.left)
        right_height = maxdepth(root.right)
        return max(left_height,right_height)+1 

 
#110. Balanced Binary Tree !!IMPORTANT
"""
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        #use -1 to mark as the height of right - left >1 
        #use a helper funciton to return the height differences 
        def helper(root):
            if not root: #reach the end , there is no left or right node
                return 0 
            left , right  = helper(root.left), helper(root.right)
            if abs(left-right)>1 or left ==-1 or right == -1: #hardest part 
                return -1
            return max(left,right)+1
            
        return helper(root)!=-1 

def isBalanced(self, root):
    self.balanced = True
    def height(root):
        if not root or not self.balanced:
            return -1
        lf,rh = height(root.left), height(root.right)
        if abs(lf-rh)>1:
            self.balanced = False
            return -1    
        return max(lf,rh)+1
    
    height(root)
    return self.balanced


    
#112. Path Sum !!IMPORTANT
"""
given sum = 20 
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true because 
5->4->11 
"""
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    #three unit case, 
    #1. node at the bottom, stop 
    #2. node has single child, pass to next level but one of the node will be None exception 
    #3. node both left and right, check the value and move to the nxt one 
    if not root:
        return False #case 2 
    if not root.left and not root.right: #case 1 
        return sum - root.val == 0
    else:
        sum -= root.val #case 3, move down 
    left = self.hasPathSum(root.left, sum)
    right = self.hasPathSum(root.right,sum)

    return left or right 

#100. Same Tree
"""
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
"""
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and q:
        return True
    if not p or q:
        return False 
    if p and q:
        right = self.isSameTree(p.right, q.right)
        left = self.isSameTree(p.left, q.left)
        return (p.val == q.val and right and left)

#101. Symmetric Tree
"""
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3

"""   
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return False 
    #use search function to compare two node value, starting from left and right 
    # then compare right.right == left.left or right.left == left.right  
    #need a new function to compare left and right 
    def dfs(left,right)->bool:
        if not left and not right:
            return True 
        if not left or not right:
            return False 
        if left.val != right.val:
            return False 
        return (dfs(right.right, left.left) and dfs(right.left, left.right))
    
    return dfs(root.left, root.right)


#108. Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    num_left = nums[:mid]
    num_right = nums[mid+1:]

    root.left = self.sortedArrayToBST(num_left)
    root.right = self.sortedArrayToBST(num_right)

    return root 
0,1,2,3
1,2,3,4

#226. Invert Binary Tree
"""
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
        return None
    #ignore the case when root dose not have children, swap then, 
    #and the process will stop in the next recursive call to check root value 
    root.left, root.right = root.right, root.left 

    self.invertTree(root.left)
    self.invertTree(root.right)

    return root 

#111. Minimum Depth of Binary Tree
"""
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0 
    if not root.right or root.left:
        return max(self.minDepth(root.right),self.minDepth(root.left))+1 #one of the count will be 0 
    if root.right and root.left:
        return min(self.minDepth(root.right),self.minDpeth(root.max))+1


#257. Binary Tree Paths
"""
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
"""
def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #need to have a way to traverse the tree
    #option 1 dfs-> as a function and pass in the leaf note to traverse
    #option 2 use stack to preserve the node to traverse, move to a new node add to the stack 
    self.result =[]
    if not root:
        return self.result 
    else:
        self.dfs(root,"")
        return self.result  #defined as a function 

def dfs(self,root,string):
    if not root.right and not root.left:
        self.result.append(string + str(root.val))
    if root.right:
        self.dfs(root.right, string+ str(root.val)+"->")
    if root.left:
        self.dfs(root.left, string+str(root.val)+"->")

#or write as higher order funciton 
def binaryTreePaths2(self, root: TreeNode) -> List[str]:
    self.result =[]
    def dfs(root,string):
        if not root.right and not root.left:
            self.result.append(string + str(root.val))
        if root.right:
            dfs(root.right, string+ str(root.val)+"->")
        if root.left:
            dfs(root.left, string+str(root.val)+"->")

    if not root:
        return self.result 
    else:
        dfs(root,"")
        return self.result  #defined as a function 


#235. Lowest Common Ancestor of a Binary Search Tree
"""
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None 

        while root:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val< min(p.val,  q.val):
                root=root.right 
            else:
                return root
    


#687. Longest Univalue Path
"""
nput:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2
depth first search, need to find the max path and then add up 
reset the path if there is no match  
"""
def longestUnivaluePath(root: TreeNode) -> int:
    #we need to know the max path of left and right
    #if left or right match to the root, add 1 otherwise reset to 0 
    max_path = 0 
    def dfs(node, path):
        if not node:
            return 0 
        #traverse to the botton     
        left_path = dfs(node.left,path)
        right_path = dfs(node.right,path)

        #check the matching logic 
        left_path += 1 if node.left and node.left.val == node.val else 0 
        right_path += 1 if node.right and node.right.val == node.val else 0 

        path = max(path, left_path+right_path)

        return max(left_path, right_path)

#Tree Traversal 
"""
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
#DFS 
#1 revursiev 
def rightSideView(root:TreeNode, level:int)->List[int]:
    if not root:
        return []
    right_side = []

    def helper(node, level):
        if level == len(level):
            right_side.append(node.val)
        for child in [root.right, root.left]:
            if child:
                helper(child,level+1)
        
        helper(root,0)
        return right_side

#BFS
#iterative with queue 
def rightSideView(root:TreeNode, level:int)->List[int]:
    if not root:
        return []
    right_side = []
    next_level =deque([root])

    while next_level:
        cur_level = next_level
        next_level = deque()
        
        while cur_level:
            node = cur_level.popleft()
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        right_side.append(node.val)
    return right_side


nums = [10,1,2,4,7,2]
limit = 5

cur_length = 0
max_length = 0 
start = nums[0]
for i in nums[1:]:
    if abs(start-i)<=limit:
        cur_length+=1
        start = min(nums,i)
        print(i,'current length{}'.format(cur_length))
    if abs(start-i)>limit:
        start = i
        max_length = max(max_length, cur_length)
        print(i,'current max length{}'.format(max_length))
        cur_length = 0 



