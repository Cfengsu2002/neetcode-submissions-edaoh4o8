# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isTrue=False
        if  p==None and q==None:
            return True
        def dfs(node1, node2):
            nonlocal isTrue
            if node1==None:
                return
            if node1!=None and node2!=None and node1.val==node2.val and isTrue==False:
                isTrue=self.compare(node1, node2)
            dfs(node1.left, node2)
            dfs(node1.right, node2)
            return
        dfs(p,q)
        return isTrue


    def compare(self, father_tree, son_tree):
        if father_tree==None and son_tree!=None:
            return False
        if father_tree!=None and son_tree==None:
            return False
        if father_tree==None and son_tree==None:
            return True
        if father_tree.val!=son_tree.val:
            return False
        return self.compare(father_tree.left, son_tree.left) and self.compare(father_tree.right, son_tree.right)