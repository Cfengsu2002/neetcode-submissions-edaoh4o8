class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L=0
        R=len(nums)-1
        while(L<=R):
            median=(L+R)//2
            if(nums[median]==target):
                return median
            elif(nums[median]>target):
                R=median-1
            else:
                L=median+1
        return -1