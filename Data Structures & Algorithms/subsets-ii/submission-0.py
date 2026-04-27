class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans_list=[]
        ans_list.append([])
        nums.sort()
        def dfs(cur_list, index):
            nonlocal ans_list
            if(index>=len(nums)):
                return
            cur_list.append(nums[index])
            ans_list.append(cur_list.copy())
            dfs(cur_list, index+1)
            cur_list.pop()
            # skip the same value
            while(index+1<=len(nums)-1 and nums[index+1]==nums[index]):
                index+=1
            dfs(cur_list, index+1)
            return
        dfs([], 0)
        return ans_list