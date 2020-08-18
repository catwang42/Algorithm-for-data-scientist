#Find Permutation 
"""
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", 
where the number 1 and 2 construct an increasing relationship.

Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]

"""

def findPermutation(self, s: str) -> List[int]:
    stack = []
    res = []

    for i in range(s):
        if s[i] == 'I':
            stack.append(i)
            while(stack):
                res.append(stack.pop())
        else:
            stack.append(i)
    
    stack.append(len(s)+1)
    while stack:
        res.append(stack.pop())
        
    return res 

    

