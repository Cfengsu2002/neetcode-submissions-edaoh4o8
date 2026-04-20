# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs_diameter(node):
            nonlocal ans
            if not node:
                return 0
            left = dfs_diameter(node.left)
            right = dfs_diameter(node.right)
            ans=max(left+right, ans)
            return 1+max(left, right)
        dfs_diameter(root)
        return ans 