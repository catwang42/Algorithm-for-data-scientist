#2. Add Two Numbers
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    sum_list= ListNode()
    temp = sum_list #an temp mode to establish link to others 
    sum_val, pass_val = 0,0 

    #check num for the case [5]+[5] =[0][1]
    while l1 and l2 and pass_val:
        sum_val = pass_val
        if l1: #for uneven l1 and l2
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        new_node = ListNode(sum_val%10)
        temp.next = new_node
        pass_val = sum_val//10
        temp = temp.next

    return sum_list.next
