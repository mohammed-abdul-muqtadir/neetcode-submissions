# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        d = collections.deque()
        d.append(root)

        while d:
            dLen = len(d)
            lvl = []
            for i in range(dLen):
                node = d.popleft()
                if node:
                    lvl.append(node.val)
                    d.append(node.left)
                    d.append(node.right)
                
            if lvl:
                ans.append(lvl)
        
        return ans
                






