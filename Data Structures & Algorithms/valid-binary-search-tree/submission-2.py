# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list=[]
        def inorder_dfs(node):
            nonlocal inorder_list
            if(node==None):
                return 
            inorder_dfs(node.left)
            inorder_list.append(node.val)
            inorder_dfs(node.right)
            return
        inorder_dfs(root)
        print(inorder_list)
        for i in range(1, len(inorder_list)):
            if(inorder_list[i-1]>=inorder_list[i]):
                return False
        return True