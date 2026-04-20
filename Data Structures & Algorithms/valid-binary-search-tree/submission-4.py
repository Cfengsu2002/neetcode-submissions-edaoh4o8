# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans_list=[]
        def pre_order_traversal(node):
            nonlocal ans_list
            if node==None:
                return
            pre_order_traversal(node.left)
            ans_list.append(node.val)
            pre_order_traversal(node.right)
            return
        pre_order_traversal(root)
        print(ans_list)
        compare_list=sorted(ans_list)
        return True if(compare_list==ans_list and len(ans_list)==len(set(ans_list))) else False