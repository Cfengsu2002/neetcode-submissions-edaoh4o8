class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def dfs(current=[], index=0):
            nonlocal answer
            answer.append(current.copy())
            for i in range(index, len(nums)):
                current.append(nums[i])
                dfs(current, i+1)
                current.pop()
            return
        dfs()
        return answer
        # time complexity: O(n^2) space complexity: O(n^2)
