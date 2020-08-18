#Numbers with sameconsecutive differences 
'''
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
'''

def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
    #if N ==1, return 0-9 
    if N == 1 :
        return [i for i in range(10)]
    
    #use depth first search, 
    def DFS(N, num):
        #till reach the end of the edge, append the number 
        if N == 0:
            return ans.append(num)
        #get the tail of the current number 
        tail = num % 10
        next_digits = set([tail + K, tail -K])
        for d in next_digits:
            if 0<= d < 10:
                #create new value, append to the end of the existing value 
                next_num = num*10 +d
                #recursively call DFS 
                DFS(N-1, next_num)
    ans = []
    for i in range(1,10):
        DFS(N-1, i)
    
    return list(ans)

