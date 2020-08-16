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