# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
            
        
        def rev(curr):

            pre = None
            while curr:
                nex = curr.next
                curr.next = pre
                pre = curr
                curr = nex
            
            return pre

        river = rev(head)
        x = river
        if n == 1:
            return rev(river.next)

        for i in range(1,n-1):
            x = x.next
        
        print(x.val)
        if x.next:

            x.next = x.next.next
        
        else:
            x.next = None

        return rev(river)





