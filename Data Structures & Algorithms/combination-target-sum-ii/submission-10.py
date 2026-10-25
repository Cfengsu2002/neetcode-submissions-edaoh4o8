class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(current, index):
            if(sum(current)==target):
                res.append(current.copy())
                return
            if sum(current)>target or index>=len(candidates):
                return
        
            current.append(candidates[index])
            dfs(current, index+1)
            current.pop()


            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            dfs(current, index+1)
        dfs([], 0)
        return res

