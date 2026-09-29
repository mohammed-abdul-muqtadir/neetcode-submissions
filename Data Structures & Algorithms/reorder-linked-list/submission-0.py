# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        def rev(curr):

            pre = None

            while curr:
                nex = curr.next
                curr.next = pre
                pre = curr
                curr = nex
            
            return pre
        
        second = rev(slow.next)
        slow.next = None

        first = head

        while second:
            
            t1, t2 = first.next, second.next

            first.next = second
            second.next = t1

            first, second = t1,t2
            





