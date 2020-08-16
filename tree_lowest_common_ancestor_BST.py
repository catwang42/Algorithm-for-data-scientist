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
    

