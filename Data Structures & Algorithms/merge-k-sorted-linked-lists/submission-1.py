# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)

        if k == 0:
            return None
        
        sot = []
        for i in lists:
            while i:

                sot.append(i.val)
                i = i.next
        sot = sorted(sot)
        
        x = ListNode(0)
        h = x
        for i in range(len(sot)):
            node = ListNode(sot[i])
            h.next = node
            h = h.next
        return x.next
        

        