# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node==None:
                return node
            node_left=invert(node.left)
            node_right=invert(node.right)
            node.left=node_right
            node.right=node_left
            return node
        invert(root)
        return root
