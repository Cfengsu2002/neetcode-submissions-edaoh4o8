# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque()
        queue.append(root)
        ans=[]
        while(queue):
            temp_list=[]
            for i in range(len(queue)):
                temp_node=queue.popleft()
                if(temp_node!=None):
                    temp_list.append(temp_node.val)
                if(temp_node and temp_node.left):
                    queue.append(temp_node.left)
                if(temp_node and temp_node.right):
                    queue.append(temp_node.right)
            ans.append(temp_list.copy())
        return ans if ans !=[[]] else []