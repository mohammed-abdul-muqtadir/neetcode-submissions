class Node:

    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        pre = self.right.prev
        nex = self.right
        pre.next = node
        nex.prev = node
        node.next = nex
        node.prev = pre

    def remove(self, node):
        pre = node.prev
        nex = node.next
        pre.next = nex
        nex.prev = pre

    def get(self, key: int) -> int:
        
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
        node = Node(key,value)
        self.dic[key] = node
        self.insert(node)

        if len(self.dic) > self.cap:
            node = self.left.next
            self.remove(node)
            del self.dic[node.key]








