#687. Longest Univalue Path
"""
nput:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2
depth first search, need to find the max path and then add up 
reset the path if there is no match  
"""
def longestUnivaluePath(root: TreeNode) -> int:
    #we need to know the max path of left and right
    #if left or right match to the root, add 1 otherwise reset to 0 
    max_path = 0 
    def dfs(node, path):
        if not node:
            return 0 
        #traverse to the botton     
        left_path = dfs(node.left,path)
        right_path = dfs(node.right,path)

        #check the matching logic 
        left_path += 1 if node.left and node.left.val == node.val else 0 
        right_path += 1 if node.right and node.right.val == node.val else 0 

        path = max(path, left_path+right_path)

        return max(left_path, right_path)