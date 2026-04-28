class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)]

        col_check = set()
        positive_check = set()  
        negative_check = set()  

        def dfs(y):
            if y >= n:
                ans.append(["".join(row) for row in board])
                return 
            for x in range(n):
                if x in col_check or (y + x) in positive_check or (y - x) in negative_check:
                    continue

                board[y][x] = "Q"
                col_check.add(x)
                positive_check.add(y + x)
                negative_check.add(y - x)

                dfs(y + 1)

                col_check.remove(x)
                positive_check.remove(y + x)
                negative_check.remove(y - x)
                board[y][x] = "."

        dfs(0)
        return ans