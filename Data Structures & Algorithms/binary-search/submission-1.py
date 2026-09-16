class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        L = 0
        R = len(nums) - 1

        while L <=R:
            midlle=(L+R)//2
            if(nums[midlle]==target):
                return midlle
            if(nums[midlle]<target):
                L=midlle+1
            else:
                R=midlle-1
        return -1