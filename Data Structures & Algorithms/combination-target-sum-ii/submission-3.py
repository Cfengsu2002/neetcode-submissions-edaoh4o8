class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # two_branch_each_time
        ans=[]
        candidates.sort()
        def dfs(index, subranch):
            nonlocal ans
            if(sum(subranch)==target):
                ans.append(subranch.copy())
                return
            if sum(subranch) > target:
                return
            if(index>=len(candidates)):
                return
            subranch.append(candidates[index])
            dfs(index+1, subranch)
            subranch.pop()
            while(index + 1 < len(candidates) and candidates[index+1]==candidates[index]):
                index+=1
            dfs(index+1, subranch)
            return
        dfs(0, [])
        return ans 