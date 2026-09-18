class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        dp=[0]*len(nums)
        for i in range(len(nums)-3,-1,-1):
            dp[i] = max(dp[i+2]+nums[i], dp[i+1])
        print(nums)
        print(dp)
        return dp[0]