class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_list=[1]*(len(nums))
        print(dp_list)
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, len(nums)):
                if(nums[j]>nums[i]):
                    dp_list[i]=max(dp_list[j]+1, dp_list[i])
        print(max(dp_list))
        return max(dp_list)