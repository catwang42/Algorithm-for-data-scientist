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

