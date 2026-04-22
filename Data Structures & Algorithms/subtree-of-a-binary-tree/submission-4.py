# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        is_true=False
        def dfs(node):
            nonlocal is_true
            if(node==None):
                return
            if node.val == subRoot.val:
                if compared(node, subRoot):
                    is_true = True
                    return
            dfs(node.left)
            dfs(node.right)
            return


        def compared(tree, subtree):
            if tree is None and subtree is None:
                return True
            if tree is None or subtree is None:
                return False
            if tree.val != subtree.val:
                return False

            return compared(tree.left, subtree.left) and compared(tree.right, subtree.right)
        dfs(root)
        return is_true