#Prtition list 
"""
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.
The most important tips are: 1, one node anchor as the begining (head) 2. one node to traverse
"""
class Solution:


        #when traversing linkedin list, always preserve the original list 
        #and use a node to traverse the linked list 
        left_node = ListNode()
        right_node = ListNode()
        node_l, node_r = left_node, right_node  
        
        while head is not None:
            if head.val < x:
                node_l.next = head  #add to node 
                node_l = node_l.next  #move node to next one 
            else:
                node_r.next = head 
                node_r = node_r.next

            head = head.next #move the original list curser 
        
        node_l.next = right_node.next #linked the left list last node to right list first node 
        node_r.next = None 
        
        return left_node.next