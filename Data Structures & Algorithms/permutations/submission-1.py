class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(current, visited):
            if len(current) == len(nums):
                ans.append(current.copy())
                return

            for i in range(len(nums)):
                if i in visited:
                    continue

                current.append(nums[i])
                visited.add(i)

                dfs(current, visited)

                current.pop()
                visited.remove(i)

        dfs([], set())
        return ans