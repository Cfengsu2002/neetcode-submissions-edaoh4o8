# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        true_false=True
        def dfs(node):
            nonlocal true_false
            if not node:
                return 0
            node_left_height=dfs(node.left)
            node_right_height=dfs(node.right)
            if(abs(node_left_height-node_right_height)>1):
                true_false=False
            return 1+max(node_left_height, node_right_height)
        dfs(root)
        return true_false