# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        lis = []

        def dfs(root):
            if not root:
                lis.append(None)
                return

            lis.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
      

        s = ""

        for i in lis:
            s+= str(i) + "#"
      
        return s



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        lis = data.split("#")[:-1]
      

        for i in range(len(lis)):
            if lis[i] == "None":
                lis[i] = None
            else:
                lis[i] = int(lis[i])

        q = deque(lis)

        def dfs():
            if not q:
                return None

            val = q.popleft()
            if val == None:
                return None
            
            n = TreeNode(val)
            n.left = dfs()
            n.right = dfs()

            return n
        
        return dfs()
            



        

