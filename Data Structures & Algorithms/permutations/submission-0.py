class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans_list=[]

        def dfs(parameter_list, cur_list):
            nonlocal ans_list
            if(len(cur_list)==len(nums)):
                ans_list.append(cur_list.copy())
                return
            if(len(parameter_list)==0):
                return
            for i in range(len(parameter_list)):
                new_list=parameter_list[:i]+parameter_list[i+1:]
                cur_list.append(parameter_list[i])
                dfs(new_list, cur_list)
                cur_list.pop()
            return
        dfs(nums, [])
        return ans_list