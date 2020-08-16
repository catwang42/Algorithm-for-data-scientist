#PROBLEM 
"""
Given an array of 1s and 0s. Your method should return midpoint of the longest subarray of zeros.
0100010=> 3
"""
def test_funciton():
    assert findMidZero([0,1,0,0,0,1,0]) == 3, "Test result failed"

def findMidZero(alist:Link[int])->int:
    cur_length = 0 
    max_lengh = 0 
    start = 0 
    for i in alist:
        if alist[i] == 0:
            cur_length += 1
        else:
            start = i+1
            max_lengh = max(max_lengh, cur_length)
            cur_length = 0 
    
    #if 0 is at the end of string 
    if cur_length > max_lengh:
        start = len(alist) - cur_length
        max_lengh = cur_length

    return start+max_lengh//2
