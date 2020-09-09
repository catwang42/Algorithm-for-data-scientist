"""
Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
#Dynamic programming
import math 
def numSquares(self, n: int) -> int:
    #find all the possible square value 
    squares = [i**2 for i in range(int(math.sqrt(n))+1)]

    # remembering all the subsolution in a dp list 
    # we need to find the smallest value, so initialise the list to be infinite large
    dp=[float("inf")]*(n+1)
    dp[0] = 0 

    #looping through the value, and find the minimal perfect square for each sub solution
    for i in range(1,n+1):
        for square in squares:
            if square>i :
                break 
            dp[i]=min(dp[i],dp[i-square]+1)
    
    return dq[-1]


