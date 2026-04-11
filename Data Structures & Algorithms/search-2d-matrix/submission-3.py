class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        target_row=-1
        L=0
        R=len(matrix)-1
        while(L<=R):
            M=(L+R)//2
            if(matrix[M][0]<=target<=matrix[M][len(matrix[0])-1]):
                target_row=M
                break
            elif(matrix[M][0]<=matrix[M][len(matrix[0])-1]<=target):
                L=M+1
            else:
                R=M-1
        if(target_row==-1):
            return False
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