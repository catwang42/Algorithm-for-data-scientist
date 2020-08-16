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
