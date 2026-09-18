class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        is_true=False
        visited=set()
        def dfs(y, x, index):
            nonlocal is_true
            if(index==len(word)):
                is_true=True
                return
            if(y<0 or y>=len(board) or x<0 or x>=len(board[0])):
                return 
            if ((y,x) in visited):
                return
            if(board[y][x]!=word[index]):
                return
            visited.add((y,x))
            dfs(y+1,x,index+1)
            dfs(y-1,x,index+1)
            dfs(y,x+1,index+1)
            dfs(y,x-1,index+1)
            visited.remove((y,x))
            return
        for y in range(len(board)):
            for x in range(len(board[0])):
                dfs(y,x,0)
        return is_true

            
            
        