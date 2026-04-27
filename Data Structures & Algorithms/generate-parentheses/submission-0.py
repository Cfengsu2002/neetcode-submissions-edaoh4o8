class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_list=[]

        def dfs(left_count, right_count, cur_str):
            nonlocal ans_list
            if(right_count>left_count):
                return
            if(left_count>n):
                return
            if(right_count==n and left_count==right_count):
                ans_list.append(cur_str)
                return
            dfs(left_count+1, right_count, cur_str+"(")
            dfs(left_count, right_count+1, cur_str+")")
            return
        dfs(0,0,"")
        return ans_list