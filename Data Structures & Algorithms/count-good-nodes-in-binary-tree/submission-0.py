# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_node_number=0 # it is because room is considered one also
        def good_node_count(node, cur_max_node):
            nonlocal good_node_number
            if node==None:
                return cur_max_node
            if(node.val>=cur_max_node):
                good_node_number+=1
            good_node_count(node.left, max(node.val, cur_max_node))
            good_node_count(node.right, max(node.val, cur_max_node))
            return cur_max_node
        good_node_count(root, root.val)
        return good_node_number
