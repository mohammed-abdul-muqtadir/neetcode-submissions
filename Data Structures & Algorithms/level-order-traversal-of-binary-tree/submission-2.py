# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def dfs(node,d):
            if not node:
                return None
            if len(ans) == d:
                ans.append([])
            
            ans[d].append(node.val)
            dfs(node.left,d+1)
            dfs(node.right,d+1)
        
        dfs(root,0)
        return ans