# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isTrue=True
        def dfs(root):
            nonlocal isTrue
            if root==None:
                return 0
            left_child=dfs(root.left)
            right_child=dfs(root.right)
            if(abs(left_child-right_child)>1):
                isTrue=False
                return 0
            return max(left_child, right_child)+1
        dfs(root)
        return isTrue