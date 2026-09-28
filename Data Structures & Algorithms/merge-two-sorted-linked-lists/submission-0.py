# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if not list1:
                return list2
            if not list2:
                return list1

            if list1.val > list2.val:
                list1,list2 = list2,list1
            
            head = list1

            curr1, curr2 = list1, list2

            while curr1.next and curr2:

                if curr1.val <= curr2.val <= curr1.next.val:

                    nex2 = curr2.next

                    curr2.next = curr1.next
                    curr1.next = curr2


                    curr1 = curr2
                    curr2 = nex2
                
                else:
                    curr1 = curr1.next

            
            
            if curr2:
                curr1.next = curr2

            return head





