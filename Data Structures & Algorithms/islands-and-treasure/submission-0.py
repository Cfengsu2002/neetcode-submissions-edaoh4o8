class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        def update_grid(y, x):
            visited=set()
            queue=deque()
            queue.append([(y,x),0])
            directions=[[1,0], [-1,0], [0,1], [0,-1]]
            while(queue):
                cur_point=queue.popleft()
                y,x=cur_point[0]
                distance=cur_point[1]
                visited.add((y,x))
                for direction in directions:
                    ny, nx=y+direction[0], x+direction[1]
                    if(len(grid)-1>=ny>=0 and len(grid[0])-1>=nx>=0  and grid[ny][nx]!= -1 and grid[ny][nx]!=float('inf')):
                        if (ny, nx) not in visited:
                            grid[ny][nx]=min(grid[ny][nx], distance+1)
                            queue.append(((ny,nx), distance+1))







        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]==0:
            
                    update_grid(y,x)