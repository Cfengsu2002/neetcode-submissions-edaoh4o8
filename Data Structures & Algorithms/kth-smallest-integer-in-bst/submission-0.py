# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # for this question I want to solve it with inorder traversal 
        ans=[]
        def dfs(root):
            nonlocal ans
            if(len(ans)==k):
                return
            if(root==None):
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
            return
        dfs(root)
        print(ans)
        return ans[k-1]