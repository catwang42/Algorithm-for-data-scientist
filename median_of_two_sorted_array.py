#PROBLEM 
#4. Median of Two Sorted Array 
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #left and right pointer, merge sort into one 
        #when (m+n) %2 == 0  , then return (mid +(mid-1))/2 
        #when (m+n) %2 != 0 , then return mid 
        
        left , right = 0, 0 
        join = []
        
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                join.append(nums1[left])
                left += 1
            else:
                join.append(nums2[right])
                right +=1
        join += nums1[left:] # cannot use append, otherwise will be a nested array 
        join += nums2[right:]
        
        mid = len(join)//2
        
        if len(join) %2 != 0:
            return join[mid]
        else:
            return ((join[mid] + join[mid-1])/2)