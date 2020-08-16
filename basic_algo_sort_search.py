
#Algorithms 
"""
Search: Binary Search , DFS, BFS
Sort: 
"""
#bubble sort -> compare a pair and iterate though 𝑂(𝑛2)

#insertion sort 
"""
Time Complexity: 𝑂(𝑛2), 
Space Complexity: 𝑂(1)
"""
from typing import List, Dict, Tuple, Set
def insertionSort(alist:List[int])->List[int]:
    #check from index 1 
    for i in range(1,len(alist)):
        currentValue = alist[i]
        while (i-1)>0 and alist[i-1]>currentValue: #if current value less than lagest, move forward 
            alist[i]=alist[i-1]
            i -= 1 
        alis[i] = currentValue #if larger than current value, don't move 

#Merge Sort
"""
Time Complexity: 𝑂(𝑛log𝑛)
Space Complexity: 𝑂(𝑛)
"""
def merge(left:List[int],right:List[int])->List[int]:
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index]<=right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index +=1
    
    #one of the list will end first and leaving the other list unmerged
    #so append the remaining list to the result 
    result += left[left_index:]
    result += right[right_index:]
    return result 

def merge_sort(alist=List[int])->List[int]:
    #need to build a base case first 
    #recursion can only happend in the else  
    if len(alist)<=1:
        return alist
    
    mid = len(alist)//2 
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])
        
    return merge(left_list, right_list)

def create_array(size=10, max=50):
    from random import randint
    return [randint(0,max) for _ in range(size)]

merge_sort(array)


#quick sort
"""
Time Complexity: average 𝑂(𝑛log𝑛), worest 𝑂(𝑛2)
Space Coplexity: 𝑂(𝑛log𝑛) 
check the validility , this print out the value 
"""
def quickSort(l:int,h:int,alist:List[int])->List[int]:
    while(h>l):
        pivot = partition(l,h,alist)
        quickSort(l,pivot-1,alist)
        quickSort(pivot,h,alist)

def partition(l,h,alist):
    pivot = alist[l]
    i, j = l, h 
    while(i<j):
        if alist[i]<=pivot:
            i +=1 
        if alist[j]>=pivot:
            j -=1
    i, j = j, i 
    pivot, j = j , pivot
    return j 


#Heapsort 

#binary search 
def binarySearch(alist:List[int], num:int)->bool:
    first = 0 
    last = len(alist)-1
    result = False
    
    while last >= first and not result: #be careful when checking the logic 
        mid = (last+first)//2 
        if num == alist[mid]:
            result = True 
        else:
            if num < alist[mid]:
                last = mid-1
            else:
                first = mid+1

    return result 

alist = [2,7,19,34,53,72]
print(binarySearch(alist,34))


#depth first search

#breadth first search  