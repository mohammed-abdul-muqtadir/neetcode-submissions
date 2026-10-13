# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        q = collections.deque()
        q.append(root)

        while q:
            lvl = []
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if lvl:
                ans.append(lvl)

        res = []

        for i in ans:
            res.append(i[-1])
        
        
        return res