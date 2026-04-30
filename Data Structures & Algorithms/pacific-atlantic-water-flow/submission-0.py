class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_land=set()
        atlantic_land=set()
        # add edges to both
        for y in range(len(heights)):
            pacific_land.add((y,0))
            atlantic_land.add((y,len(heights[0])-1))
        for x in range(len(heights[0])):
            pacific_land.add((0, x))
            atlantic_land.add((len(heights)-1,x))
        pacific_queue=deque(list(pacific_land))
        atlantic_queue=deque(list(atlantic_land))
        
        directions=[[0,1],[0,-1],[1,0], [-1,0]]
        # add land to land
        while pacific_queue:
            old_y, old_x=pacific_queue.popleft()
            for direction in directions:
                new_y, new_x=old_y+direction[0], old_x+direction[1]
                if((new_y, new_x) in pacific_land):
                    continue
                elif(new_y<0 or new_x<0 or new_y>=len(heights) or new_x>=len(heights[0])):
                    continue
                elif(heights[new_y][new_x]<heights[old_y][old_x]):
                    continue
                else:
                    pacific_land.add((new_y, new_x))
                    pacific_queue.append((new_y, new_x))

        while atlantic_queue:
            old_y, old_x=atlantic_queue.popleft()
            for direction in directions:
                new_y, new_x=old_y+direction[0], old_x+direction[1]
                if((new_y, new_x) in atlantic_land):
                    continue
                elif(new_y<0 or new_x<0 or new_y>=len(heights) or new_x>=len(heights[0])):
                    continue
                elif(heights[new_y][new_x]<heights[old_y][old_x]):
                    continue
                else:
                    atlantic_land.add((new_y, new_x))
                    atlantic_queue.append((new_y, new_x))
        return_land=[]
        for land in pacific_land:
            if land in atlantic_land:
                return_land.append(list(land))
        return return_land
