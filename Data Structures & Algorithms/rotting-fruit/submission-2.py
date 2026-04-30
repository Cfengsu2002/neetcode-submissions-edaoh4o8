class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        copy_grid = [[float('inf')] * len(grid[0]) for _ in range(len(grid))]

        def expand(y,x):
            nonlocal copy_grid
            visited={(y,x)}
            queue=deque([(y,x,0)])
            while queue:
                y,x,minute=queue.popleft()
                distances=[(1,0),(-1,0),(0,-1),(0,1)]
                for distance in distances:
                    dy, dx, new_minute=y+distance[0], x+distance[1], 1+minute
                    if(0<=dy<len(grid) and 0<=dx<len(grid[0])
                    and (dy,dx) not in visited
                    and grid[dy][dx]!=0
                    ):
                        visited.add((dy,dx))
                        copy_grid[dy][dx]=min(copy_grid[dy][dx], new_minute)
                        queue.append((dy,dx,new_minute))

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]==2):
                    copy_grid[y][x]=0
                    expand(y,x)
        
        return_ans=0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x]==1):
                    return_ans=max(copy_grid[y][x], return_ans)
            
        return return_ans if return_ans!=float('inf') else -1