#206. Reverse Linked List
"""
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""        
def reverseList(self, head: ListNode) -> ListNode:
    pre = None #setting up a previouse anchor 
    next_link = None #setting up next link anchor 
    node = head 

    while node:
        next_node= node.next #need to preserve the link to next node 
        node.next = pre
        pre = node 
        node = next_node 
    return pre
