#4. merge two linked list 
class ListNode:
    def __init__(self):
        self.val = 0
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: 
            return None 
        
        node = ListNode() #node to traverse throught the linked list 
        merged = node #merge as the anchor to the return linkedlist 
        
        if l1.val<=l2.val:
            #linked smaller node to merged list 
            node.next=l1
            #move link point to l1 next node object 
            l1 = l1.next 
        else:
            node.next, l2 = l2, l2.next 

        #when finish looping one of the linked list     
        if not l1 or l2:
            node.next =  l1.next or l2.next 
        
        #node has become a pointer of last item of l1 and l2, 
        #so return the reserved merged node to print the entire linked list 
        return merged.next 
 