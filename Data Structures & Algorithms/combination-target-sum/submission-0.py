class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans_list = []

        def dfs(start, cur_list, cur_sum):
            if cur_sum == target:
                ans_list.append(cur_list.copy())
                return
            
            if cur_sum > target:
                return

            for i in range(start, len(nums)):
                cur_list.append(nums[i])
                dfs(i, cur_list, cur_sum + nums[i])
                cur_list.pop()

        dfs(0, [], 0)
        return ans_list