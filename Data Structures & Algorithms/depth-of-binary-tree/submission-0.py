# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth=0
        def dfs(node, level):   
            nonlocal max_depth
            if node==None:
                max_depth=max(max_depth, level)
                return None
            node_left=dfs(node.left, level+1)
            node_right=dfs(node.right, level+1)
            return node
        dfs(root, 0)
        return max_depth