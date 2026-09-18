class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer_list=[]
        def dfs(answer, index):
            nonlocal candidates, answer_list
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                answer.append(candidates[i])
                if(sum(answer)==target and answer not in answer_list):
                    answer_list.append(answer.copy())
                    answer.pop()
                    return
                if(sum(answer)>target):
                    answer.pop()
                    return 
                dfs(answer, i+1)
                answer.pop()
            return 
        dfs([], 0)
        return answer_list            
