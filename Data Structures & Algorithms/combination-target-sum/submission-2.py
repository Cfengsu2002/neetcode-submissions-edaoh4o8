class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        answer_list = []

        def dfs(answer, index):

            for i in range(index, len(nums)):

                answer.append(nums[i])

                if sum(answer) == target:
                    answer_list.append(answer.copy())
                    answer.pop()
                    continue

                if sum(answer) > target:
                    answer.pop()
                    break

                # 注意这里是 i，不是 i + 1
                # 因为当前数字可以重复使用
                dfs(answer, i)

                answer.pop()

        dfs([], 0)

        return answer_list