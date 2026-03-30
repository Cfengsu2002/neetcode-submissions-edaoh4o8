class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                remain=target-nums[i]
                if(nums[j]==remain):
                    return [i,j]
