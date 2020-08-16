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
