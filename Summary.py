#MATRIX 
# 1. transpose of a matrix
matrix = [[1,2,3,4],[4,5,6,7]]
transp_matrix = [[row[i] for row in matrix]for i in range(len(matrix[0])) ]


#STRING #2.2 longest common subsequence 
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


#PROBLEM 
#14. Longest Common Prefix
"""
Input: ["flower","flow","flight"]
Output: "fl"
"""
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ''
    #find the shorest len 
    min_str_len = min([len(w) for w in strs])

    prefix = ''
    for i in range(min_str_len):
        is_prefix = strs[0][i]

        if all([word[i] == is_prefix for word in strs]):
            prefix += is_prefix
        else:
            break #if not added, will return all match case (abc, dec)-> c
    return prefix

# 123 + 286 
def addStrings1(num1, num2):
    i , j = len(num1)-1 , len(num2) -1
    pass_next = 0 
    result = ''

    temp1 , temp2 = 0, 0 
    
    while i >= 0 or j >= 0:
        temp1 = int(num1[i]) if i >= 0 else 0 
        temp2 = int(num2[j]) if j >= 0 else 0 
        
        result += str((pass_next + temp1 + temp2)%10)
        pass_next = (pass_next + temp1 + temp2)//10
        
        i -= 1 
        j -= 1 

    if pass_next>0:
        result += str(pass_next)
    return result[::-1]

#PROBLEM 
#maxium remve one char and be palindrome 
def testPalindrome():
    assert validPalindrome('asbcba') is True , "Function error"

def validPalindrome(s: str) -> bool:
    start, end = 0, len(s)-1
    while start<end:
        if s[start] != s[end]:
            left = s[start+1:end+1]
            right = s[start:end]
            return left == left[::-1] or right == right[::-1]
            #print('left', left)
            #rint('right',right)
        start += 1 
        end -= 1
     
    return True

#EMAIL Mapping 

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails= ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
email_map =set()
for i in emails:
    import re
    host, domain = i.split("@")
    host = re.sub(r'\.','',host)
    host = host.split("+",1)[0]
    email_map.add(host+'@'+domain)

#Licese key formatting 
"""
S = "w95F3Z-2e-9-w", K = 4
 "W9-5F3Z-2E9W"
"""
def licenseKeyFormatting(S: str, K: int) -> str:
    clean_s = S.replace('-','').upper()[::-1]
    plate_list = [clean_s[i:i+K] for i in range(0,len(clean_s),K)]
    result = '-'.join(plate_list)
    return result[::-1]

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

#PROBLEMS 
#sort log 
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def unitTest():
    assert reorderLogFiles(logs) == ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"] , "Failed test"

def reorderLogFiles(logs):
    def custom_sort(log):
        _id, contetn = log.split(" ",1)
        return (0, contetn, _id) if contetn[0].isalpha() else (1,)
    
    return sorted(logs,key=custom_sort)

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

#PROBLEM best time to sell stock 
def testFun():
    assert maxProfit([7,1,5,3,6,4]) == 5, "Function failed should be 5"

def maxProfit(prices:List[int])->int:
    cur_profit = max_profit = 0 
    start = prices[0]
    n = len(prices)

    for i in range(1,n):
        if prices[i] > start:
            #cur_profit = i-start
            #print(i, "cur profit", cur_profit)
            max_profit = max(prices[i]-start,max_profit)
            print(i, "max profit", max_profit)
        if prices[i] < start and prices[i] < min(prices[:i]):
            start = prices[i]
    return max_profit

#PROBLEM 
def testMoveZeros():
    nums = [0,0,1,0,2,0,3,4]
    assert moveZeroes(nums)==[1,2,3,2,0,0,0],"Function Failed"
    

def moveZeroes( nums: List[int]) -> None:
    first_zero = None 
    for i , val in enumerate(nums):
        if val == 0 and first_zero is None:
            first_zero = i 
            #print('find fist zero index', i)
        if val != 0 and first_zero is not None:
            #print('swape number {} with zero at index {}'.format(nums[i],first_zero))
            nums[i] , nums[first_zero] =  nums[first_zero], nums[i]
            first_zero += 1 
            #print('change first zero index' ,first_zero)




################################
#MAP
#Problem 
#check Valid Parentheses
def testFun():
    assert isValid("{[]}") is True, "Funtion failed, should be True"
    assert isValid("{[]") is False, "Funtion failed, should be False"

def isValid(s:str)->bool:
    deque=[s[0]]
    mapping = {'(': ')', '{': '}', '[' : ']'}
    n = len(s)
    
    for i in range(1,n):
        if deque[-1] in mapping and mapping[deque[-1]] == s[i]:
            deque.pop()
        else:
            deque.append(s[i])
    return deque == []

#Find Unique Character 
def testFun():
    assert firstUniqueChar('loveleetcode') == 2

def firstUniqChar(self, s: str) -> int:
    if not s:
        return -1
    
    h_map = {}
    for i in range(len(s)):
        if s[i] in h_map:
            h_map[s[i]] += 1
        else:
            h_map[s[i]] = 1
    
    single = [k for (k,v) in h_map.items() if v==1]
    
    return s.index(single[0]) if single !=[] else -1

import collections 
def firstUniqueChar(s:str)->int:
    char_count = collections.Counter(s)

    for k, v in enumerate(s):
        if char_count[v] ==1:
            return k 
    return -1 





