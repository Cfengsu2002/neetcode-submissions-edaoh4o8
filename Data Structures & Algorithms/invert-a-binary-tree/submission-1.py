# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(root):
            if root == None:
                return root
            left_child = reverse(root.left)
            right_child = reverse(root.right)
            root.left= right_child
            root.right = left_child
            return root
        return reverse(root)