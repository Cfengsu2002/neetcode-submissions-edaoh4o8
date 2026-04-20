# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=deque([root])
        ans=[]
        if root==None:
            return []
        while queue:
            level_size=len(queue)
            for i in range(level_size):
                cur_node=queue.popleft()
                if(cur_node.left):
                    queue.append(cur_node.left)
                if(cur_node.right):
                    queue.append(cur_node.right)
                if(i==level_size-1):
                    ans.append(cur_node.val)
        return ans