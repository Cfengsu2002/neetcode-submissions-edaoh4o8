class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row=0
        for y in range(len(matrix)):
            if(matrix[y][0]<=target<=matrix[y][-1]):
                target_row=y
        L=0
        R=len(matrix[0])-1
        while(L<=R):
            M=(L+R)//2
            if(matrix[target_row][M]==target):
                return True
            elif(matrix[target_row][M]<target):
                L=M+1
            else:
                R=M-1
        return False