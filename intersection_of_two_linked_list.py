#160. Intersection of Two Linked Lists
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    curA ,curB = headA, headB
    
    len_A = self.lenof(curA)
    len_B = self.lenof(curB)
    
    if (len_A>len_B):
        for _ in range(len_A-len_B):
            headA = headA.next
    elif (len_B>len_A):
        for _ in range(len_B-len_A):
            headB = headB.next
    else:
        while headA != headB:
            headA = headA.next
            headB = headB.next
    return headA

def lenof(self,llist):
    count = 0 
    while llist:
        llist = llist.next
        count+=1
