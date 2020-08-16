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