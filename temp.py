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
#O(NlogN)
from typing import List, Dict, Tuple, Set
def sortedSquares(A:List[int])->List[int]:
    for i in range(len(A)):
        A[i] = A[i]**2
    A.sort()
    return A

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
#690. Employee Importance
"""
Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
"""
employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
d = 1 
def getImportance( employees, id: int) -> int:
    weight_sum = 0 

    def find_child(master, alist, child):
        if master == []:
            return [] 
        else:
            for i in master:
                child.append(alist[i-1][1])
                find_child(alist[i-1][2],alist,child)
            return child 
    all_child = find_child(employees[d-1][2], employees, [])
    weight_sum = sum(all_child)+employees[d-1][1]

    return weight_sum

getImportance(employee,d)

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
def getImportance(self, employees:List[Employee], id):
    #return of this getImportance will be getting importance for current node 
    #each node has id , value and child 
    #convert into map 
    """not optimal"""
    employee_map = {emp.id:emp for emp in employees}
    result = employee_map[id].importance

    #find child importance 
    for child in employee_map[id].subordinates:
        result += self.getImportance(employees,child)
    return result 

def getImportance1(self, employees:List[Employee], id:int)->int:
    employee_map = {emp.id: emp for emp in employees}
    #map all the employee in a hash map  
    def dfs(employee, map):
        result = employee.importance
        for child in employee.subordinates:
            result += dfs(map[child],map)
        return result 

    return dfs(employee_map[id],employee_map)



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
def testFun():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6, "Funciton Failed, should be 6 "

def maxSubArray(nums)->int:
    curr_sum = max_sum = nums[0] 
    for i in nums[1:]:
        curr_sum = max(i, curr_sum+i)
        print(i, '->' , curr_sum)
        max_sum = max(max_sum, curr_sum)
    return max_sum



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

#PROBLEM 
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


num1="123"
num2="879"


def addStrings(num1, num2):
    i , j = len(num1)-1 , len(num2) -1
    pass_next = 0 
    result = ''
    
    while i >= 0  and j >= 0:
        result += str((pass_next+int(num1[i])+int(num2[j]))%10)
        print('result', result)
        pass_next = (pass_next+int(num1[i])+int(num2[j]))//10 
        print('pass_next', pass_next)
        i -= 1 
        j -=1
    
    if i> 0 and j<0:
        while i >= 0:
            result += str((pass_next+int(num1[i]))%10)
            pass_next = (pass_next+int(num1[i]))//10 
            i -= 1
            
    if j>0 and not i<0:
        while j >= 0:
            result += str((pass_next+int(num2[j]))%10)
            pass_next = (pass_next+int(num2[j]))//10 
            j -= 1

    if pass_next>0 and i < 0 and j < 0:
        result += str(pass_next)

    return result[::-1] 

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
    #445. Add Two Numbers II

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = 0, 0
        result = []
        
        while left < len(nums1) and right < n:
            if nums1[left]<= nums2[right]:
                left += 1
            else:
                nums1.insert(left, nums2[right])
                right += 1
                left += 1
                nums1.pop()
        
        if right< n:
            nums1 = nums1[:m+right]+nums2[right:]
        return nums1 
            #print(nums1[:m+right]+nums2[right:])
            #print(nums1)
        

#PROBLEM 
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
            #return left == left[::-1] or right == right[::-1]
            print('left', left)
            print('right',right)
        start += 1 
        end -= 1
     
    return True

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



def testFun():
    assert isIsomorphic("paper","ttile") is False, "Function Failed"
    assert isIsomorphic('paper','title') is True,"Functin Failed"

def isIsomorphic(s:str,t:str)->bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s,t)))





#PROBLEM 
#flattern nested array 
"""

"""


#PROBLEM 
"""
Input:
Dictionary: { 'hello', 'cat', 'world', 'dog', 'bird', 'grass', 'green', 'help', 'greet', 'great' }
String: bbbirrrdddd
Output: True
"""
dictionary = { 'hello', 'cat', 'world', 'dog', 'bird', 'grass', 'green', 'help', 'greet', 'great' }
{word:set(word) for word in dictionary}


#PROBLEM 
"""
synonym_pairs: [('great', 'good'), ('great', 'excellent'), ('good', 'fine')]
sentence_pairs: [('Google is a good company', 'Google is a great company'), ('My performance is bad', 'My performance is poor')]
"""



#PROBLEM 
#MEETING ROOM 
"""1
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Input: [[7,10],[2,4]]
Output: 1
"""
def testFun():
    assert minMeetingRooms([[0, 30],[5, 10],[15, 20]], 2), "Test Case Failed "



