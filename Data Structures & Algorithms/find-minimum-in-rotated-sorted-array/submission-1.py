class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums) - 1
        while(l<r):
            median=(l+r)//2
            if(nums[median]>nums[r]):
                l=median+1
            else:
                r=median
        # we find the pivot point
        return nums[l]