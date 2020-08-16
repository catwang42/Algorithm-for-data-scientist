#108. Convert Sorted Array to Binary Search Tree
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    num_left = nums[:mid]
    num_right = nums[mid+1:]

    root.left = self.sortedArrayToBST(num_left)
    root.right = self.sortedArrayToBST(num_right)

    return root 
