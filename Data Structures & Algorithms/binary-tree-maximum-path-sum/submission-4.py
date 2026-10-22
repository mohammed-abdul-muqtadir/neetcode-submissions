# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        su = float("-inf")

        def dfs(root):
            if not root:
                return 0

            nonlocal su

            a = max(dfs(root.left),0)
            b = max(dfs(root.right),0)

            path = a+b+ root.val

            su = max(su,path)

            return root.val + max(a,b)
        
        dfs(root)
        return su