class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        def dfs(current=[], index=0):
            nonlocal ans
            if sum(current)==target:
                ans.append(current.copy())
                return  
            i=index
            while i < len(nums):
                if sum(current)>target:
                    return 
                current.append(nums[i])
                dfs(current, i)
                i+=1
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
                current.pop()
        
            return
        dfs()
        return ans