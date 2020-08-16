#longest common subsequence 
"""
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
The key point for this solution is to use hash table to remember the index of each character
"""
def lengthOfLongestSubstring(s:str)->int:
    if not s:
        return 0
    #start to remember the current non-repeatible substring start point 
    #max_len to record the current max len 
    #h_map to remember the newest index of each character  
    start, max_len, h_map = 0,0,{}
    for i, char in enumerate(s):
        #when finding a match, check if starting anchor is less than the duplicated index 
        if char in h_map and start<=h_map[char]:
            start = h_map[char]+1 #move the starting anchor to            
        else: 
            max_len = max(max_len, i-start+1) 
        h_map[char]=i
    return max_len
