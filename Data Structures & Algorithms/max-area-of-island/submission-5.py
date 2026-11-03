class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_land = 0
        visited = set()

        def dfs(y, x, current_land=0):
            nonlocal visited
            if (
                not 0 <= y < len(grid)
                or not 0 <= x < len(grid[0])
                or (y, x) in visited
                or grid[y][x] == 0
            ):
                return 0

            visited.add((y, x))
            return (
                dfs(y - 1, x, current_land)
                + dfs(y + 1, x, current_land)
                + dfs(y, x + 1, current_land)
                + dfs(y, x - 1, current_land)
                + 1
            )

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in visited and grid[y][x] != 0:
                    max_land = max(dfs(y, x), max_land)

        return max_land