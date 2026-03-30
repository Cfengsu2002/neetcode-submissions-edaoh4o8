class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum=[1]*len(nums)
        after_sum=[1]*len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i]=prefix_sum[i-1]*nums[i-1]
        print(prefix_sum)
        for i in range(len(nums)-1-1, -1, -1):
            after_sum[i]=after_sum[i+1]*nums[i+1]
        print(after_sum)
        for i in range(len(prefix_sum)):
            after_sum[i]=after_sum[i]*prefix_sum[i]
        return after_sum