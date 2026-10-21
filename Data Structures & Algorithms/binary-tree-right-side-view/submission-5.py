# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, ans=deque([root]), []
        if root==None:
            return []
        while queue:
            most_right=False
            for _ in range(len(queue)):
                node=queue.popleft()
                if most_right==False:
                    most_right=True
                    if node!=None:
                        ans.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        return ans
        