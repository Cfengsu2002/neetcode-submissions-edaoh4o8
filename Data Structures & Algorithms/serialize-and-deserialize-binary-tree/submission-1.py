# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans_list=[]
        def pre_order_dfs(root):
            nonlocal ans_list
            if(root==None):
                ans_list.append('None')
                return
            ans_list.append(str(root.val))
            pre_order_dfs(root.left)
            pre_order_dfs(root.right)
            return
        pre_order_dfs(root)
        return ",".join(ans_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        ptr=0
        def preorder_decode():
            nonlocal ptr
            if(ptr==len(data)):
                return None
            if(data[ptr]=='None'):
                ptr+=1
                return None
            cur_node=TreeNode(int(data[ptr]))
            ptr+=1
            cur_node.left=preorder_decode()
            cur_node.right=preorder_decode()
            return cur_node
        return preorder_decode()
