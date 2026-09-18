class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answer_list=[]
        def dfs(answer, index):
            nonlocal answer_list
            if(sum(answer)==target):
                answer_list.append(answer.copy())
                return answer
            for i in range(index, len(nums)):
                if(sum(answer)+nums[i]>target):
                    return answer
                answer.append(nums[i])
                answer=dfs(answer, i)
                answer.pop()
            return answer
        dfs([],0)
        return answer_list