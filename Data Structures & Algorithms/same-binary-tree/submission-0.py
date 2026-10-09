# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def tra(root,lis):
            if not root:
                lis.append(None)
                return None
            
            lis.append(root.val)
            tra(root.right,lis)
            tra(root.left,lis)
        
            return lis
        a = []
        b = []
        tra(p,a)
        tra(q,b)
        if a == b:
            return True
        return False