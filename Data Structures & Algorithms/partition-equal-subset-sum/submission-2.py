class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        cache={}
        total=sum(nums)
        half=total/2
        is_true=False
        def dfs(remain, index):
            nonlocal is_true
            if(is_true):
                return
            if(remain<half):
                return
            if(remain==half):
                is_true=True
                return 
            for i in range(index, len(nums)):
                dfs(remain-nums[i], i+1)
            return 
        dfs(total, 0)
        return is_true