# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')
        def dfs(root):
            nonlocal ans
            if root==None:
                return 0
            left_max_path=dfs(root.left)
            right_max_path=dfs(root.right)
            current_max_path=max(root.val, root.val+left_max_path, root.val+right_max_path)
            ans=max(current_max_path, ans, root.val+left_max_path+right_max_path)
            return current_max_path
        dfs(root)
        return ans