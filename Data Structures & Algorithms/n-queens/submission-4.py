class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(y, x, vertical, left, right, current):
            if y == n:
                answer.append([''.join(row) for row in current])
                return

            for i in range(n):
                if i in vertical or y+i in left or y-i in right:
                    continue

                vertical.add(i)
                current[y][i] = 'Q'
                left.add(y+i)
                right.add(y-i)

                dfs(y+1, i, vertical, left, right, current)

                current[y][i] = '.'
                vertical.discard(i)
                left.discard(y+i)
                right.discard(y-i)

        answer = []
        answer_board = [['.'] * n for _ in range(n)]
        dfs(0, 0, set(), set(), set(), answer_board)
        return answer