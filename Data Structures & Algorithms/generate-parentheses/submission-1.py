class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer=[]
        def dfs(left_count, right_count, current):
            if left_count==n and right_count==n:
                answer.append(current)
                return
            if right_count>left_count:
                return
            if(left_count>n):
                return 
            dfs(left_count+1, right_count, current+'(')
            dfs(left_count, right_count+1, current+')')
            return
        dfs(0,0,"")
        return answer
