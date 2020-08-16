#257. Binary Tree Paths
"""
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
"""
def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #need to have a way to traverse the tree
    #option 1 dfs-> as a function and pass in the leaf note to traverse
    #option 2 use stack to preserve the node to traverse, move to a new node add to the stack 
    self.result =[]
    if not root:
        return self.result 
    else:
        self.dfs(root,"")
        return self.result  #defined as a function 

def dfs(self,root,string):
    if not root.right and not root.left:
        self.result.append(string + str(root.val))
    if root.right:
        self.dfs(root.right, string+ str(root.val)+"->")
    if root.left:
        self.dfs(root.left, string+str(root.val)+"->")

#or write as higher order funciton 
def binaryTreePaths2(self, root: TreeNode) -> List[str]:
    self.result =[]
    def dfs(root,string):
        if not root.right and not root.left:
            self.result.append(string + str(root.val))
        if root.right:
            dfs(root.right, string+ str(root.val)+"->")
        if root.left:
            dfs(root.left, string+str(root.val)+"->")

    if not root:
        return self.result 
    else:
        dfs(root,"")
        return self.result  #defined as a function 

