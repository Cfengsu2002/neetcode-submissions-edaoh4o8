# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max=-float('inf')
        def find_max(root, cur_max):
            nonlocal global_max
            if root==None:
                return 0
            left_value=find_max(root.left, cur_max)
            right_value=find_max(root.right, cur_max)
            global_max=max(max(max(left_value, right_value)+root.val, root.val), global_max, left_value+right_value+root.val)
            cur_max=max(max(left_value, right_value)+root.val, root.val, 0)
            return cur_max
        find_max(root, 0)
        return global_max
            

            