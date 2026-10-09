class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_check(index):
            visited=set()
            for i in range(9):
                if(board[index][i] in visited):
                    print(2)
                    return False
                if(board[index][i].isdigit()):
                    visited.add(board[index][i])
            return True

        def col_check(index):
            visited=set()
            for i in range(9):
                if(board[i][index] in visited):
                    print(1)
                    return False
                if(board[i][index].isdigit()):
                    visited.add(board[i][index])
            return True        
        
        for row in board:
            print(row)

        for i in range(len(board)):
            if(not row_check(i) or not col_check(i)):
                return False
        
        square_map=defaultdict(set)
        for y in range(9):
            for x in range(9):
                y_index, x_index=y//3, x//3
                value=board[y][x]
                if(value in square_map[(y_index, x_index)]):
                    return False
                if(value.isdigit()):
                    square_map[(y_index,x_index)].add(value)
        return True






        