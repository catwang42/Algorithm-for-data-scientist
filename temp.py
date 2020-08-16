#MATRIX 
# 1. transpose of a matrix
matrix = [[1,2,3,4],[4,5,6,7]]
transp_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0])) ]



#PROBLEMS 
#find the maxium sub array , try 
def testFun():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Funciton Failed, should be 6 "

def maxSubArray(nums)->int:
    curr_sum = max_sum = nums[0] 
    for i in nums[1:]:
        curr_sum = max(i, curr_sum+i)
        print(i, '->' , curr_sum)
        max_sum = max(max_sum, curr_sum)
    return max_sum


