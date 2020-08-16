####################################
#LIST and Array 
# PROBLEM 
# Squares of a Sorted Array
"""
Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
#O(N)
def sortedSquares1( A: List[int]) -> List[int]:
    #check for positive and negative 
    for i , val in enumerate(A):
        if val > 0:
            break 
    
    negative = [pow(x,2) for x in A[:i]]
    negative.reverse()
    positive = [pow(x,2) for x in A[i:]]
    result =[]

    n_index, p_index =0,0
    #checking if either of this list is empty 
    if not negative:
        return positive 
    if not positive:
        return negative 
    #could optimise in here by checking if those two list are mutually exclusive    
    while n_index < len(negative)-1 or p_index < len(positive) -1: #important or 
        if negative[n_index] < positive[p_index]:
            result.append(negative[n_index])
            n_index += 1
        else:
            result.append(positive[p_index])
            p_index += 1

    #attach the remaining 
    result += negative[n_index:]
    result += positive[p_index:]

    return result