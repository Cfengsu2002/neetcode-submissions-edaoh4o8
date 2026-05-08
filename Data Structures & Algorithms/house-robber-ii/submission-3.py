class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        left_nums=nums[:len(nums)-1]
        right_nums=nums[1:len(nums)]
        def rob_houses(nums):
            nums=[0]+nums
            print(nums)
            for i in range(2, len(nums)):
                nums[i]=max(nums[i-1], nums[i-2]+nums[i])
            return nums[-1]
        return max(rob_houses(left_nums), rob_houses(right_nums))


