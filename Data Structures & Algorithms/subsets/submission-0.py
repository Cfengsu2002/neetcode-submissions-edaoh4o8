class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans_list=[]
        ans_list.append([])
        def dfs(cur_list, nums):
            nonlocal ans_list
            if(len(nums)==0):
                return
            for i in range(len(nums)):
                cur_list.append(nums[i])
                ans_list.append(cur_list.copy())
                dfs(cur_list, nums[i+1:])
                cur_list.pop()
            return ans_list
        dfs([], nums)
        return ans_list
