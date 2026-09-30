# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode(None)
        x = ans
        carry = 0

        while l1 or l2 or carry:
            
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            
            if total <= 9:
                x.next = ListNode(total)
                x = x.next
                carry = 0
            else:
                carry = total//10
                x.next = ListNode(total%10)
                x = x.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next


