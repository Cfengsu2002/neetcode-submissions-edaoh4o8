# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree t a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return_str=""
        queue=deque([root])
        while queue:
            node=queue.popleft()
            if not node:
                return_str=return_str+'N'
            else:
                return_str=return_str+str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            return_str=return_str+'_'
        return return_str[:-1]
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split("_")
        if values[0] == "N":
            return None
        root = TreeNode(int(values[0]))
        queue = deque([root])
        i = 1
        while queue and i < len(values):
            node = queue.popleft()
            if values[i] != "N":
                node.left = TreeNode(int(values[i]))
                queue.append(node.left)
            i += 1
            if i < len(values):
                if values[i] != "N":
                    node.right = TreeNode(int(values[i]))
                    queue.append(node.right)
                i += 1
        return root