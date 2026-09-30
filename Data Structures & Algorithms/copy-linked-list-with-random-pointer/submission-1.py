"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        dic = {None:None}
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        

        curr = head

        while curr:
            nx = dic[curr.next]
            ra = dic[curr.random]
            dic[curr].next = nx
            dic[curr].random = ra
            curr = curr.next
        
        return dic[head]

        