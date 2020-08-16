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

