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