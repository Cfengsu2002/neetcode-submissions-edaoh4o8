# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_count=0
        def dfs(root, current_max=-float('inf')):
            nonlocal good_count
            if not root:
                return 
            if root.val>=current_max:
                good_count+=1
            dfs(root.left, max(root.val, current_max))
            dfs(root.right, max(root.val, current_max))
            return current_max
        dfs(root)
        return good_count