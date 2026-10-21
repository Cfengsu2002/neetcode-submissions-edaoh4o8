class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if node is None:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            diameter = max(diameter, left_height + right_height + 2)
            return max(left_height, right_height) + 1

        dfs(root)
        return diameter