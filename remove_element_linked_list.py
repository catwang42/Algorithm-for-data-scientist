#203. Remove Linked List Elements
"""
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
def removeElements(self, head: ListNode, val: int) -> ListNode:
    #we need to preserve the current node and only checking the next value 
    #so we need to make sure the first value is not in the target 
    while head and head.val == val:
        head = head.next 
    
    #remember to keep head anchor and use a seperate node to traverse the linked list 
    #remember to use == as eual 
    node = head 
    while node:
        if node.next and node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next 
    return head 
