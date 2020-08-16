#199. Binary Tree Right Side View 
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#BFS level by level traverse 
def rightSideView(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    
    right_list=[]
    cur_level = deque([root])

    while cur_level:
        #append the right value 
        right_list.append(cur_level[-1].val)

        for i in range(len(cur_level)):
            #take the left value first 
            node = cur_level.popleft()
            if node.left:
                cur_level.append(node.left)
            if node.right:
                cur_level.append(node.right)

    return right_list   

#DFS , at each level add right child then left child, then pop out from right 
def rightSideView(self, root: TreeNode) -> List[int]:
    def dfs(root,right_list,level):
        if root:
            if level == len(right_list):
                right_list.append(root.val)
            #don't need to check the existance of left or right child, the above if root will stop on null value 
            dfs(root,root.right,level+1)
            dfs(root,root.left,level+1)
    
    right_list=[]
    dfs(root,right_list,0)

    return right_list
