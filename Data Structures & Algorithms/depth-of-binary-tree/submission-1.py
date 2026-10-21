# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height=-1
        def dfs(depth=0, root=None):
            nonlocal height
            if root == None:
                height=max(height, depth)
                return
            dfs(depth+1, root.left)
            dfs(depth+1, root.right)
            return
        dfs(0, root)
        return height



        # O(n)
        # O(n)