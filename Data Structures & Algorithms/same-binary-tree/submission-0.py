# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        is_same=True
        def dfs(p_node, q_node):
            nonlocal is_same
            if(p_node==None and q_node==None):
                return 
            elif(p_node and q_node and p_node.val==q_node.val):
                dfs(p_node.left, q_node.left)
                dfs(p_node.right, q_node.right)
                return
            else:
                is_same=False
                return 
        dfs(p,q)
        return is_same
