class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if_presented=False
        # the search algorithm
        visited=set()
        def dfs(y,x, word_index=0):
            nonlocal visited, if_presented
            if(len(word)==word_index):
                if_presented=True
                return
            if(y<0 or x<0 or y>=len(board) or x>=len(board[0]) or (y,x) in visited or board[y][x]!=word[word_index]):
                return
            visited.add((y, x))
            dfs(y+1, x, word_index+1)
            dfs(y-1, x, word_index+1)
            dfs(y, x+1, word_index+1)
            dfs(y, x-1, word_index+1)
            visited.remove((y, x))

            return
        for row in board:
            print(row)
        for y in range(len(board)):
            for x in range(len(board[0])):
                if(board[y][x]==word[0]):
                    dfs(y,x,0)
                if(if_presented):
                    return True
        return False