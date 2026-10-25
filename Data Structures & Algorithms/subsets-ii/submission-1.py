class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(index, current):
            nonlocal res
            if index>=len(nums):
                res.append(current.copy())
                return
            current.append(nums[index])
            dfs(index+1, current)
            current.pop()
            while index+1<len(nums) and nums[index]==nums[index+1]:
                index+=1
            dfs(index+1, current)
        dfs(0, [])
        return res