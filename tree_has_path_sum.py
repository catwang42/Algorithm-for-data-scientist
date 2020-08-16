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
