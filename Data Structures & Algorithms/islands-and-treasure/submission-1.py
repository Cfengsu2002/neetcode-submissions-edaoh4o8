from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    queue.append((y, x))

        while queue:
            y, x = queue.popleft()

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx

                if (
                    0 <= ny < rows
                    and 0 <= nx < cols
                    and grid[ny][nx] == INF
                ):
                    grid[ny][nx] = grid[y][x] + 1
                    queue.append((ny, nx))