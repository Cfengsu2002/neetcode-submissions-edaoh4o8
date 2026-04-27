class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return_list=[]
        def check(cur_str):
            l_ptr=0
            r_ptr=len(cur_str)-1
            while(l_ptr<=r_ptr):
                if(cur_str[l_ptr]!=cur_str[r_ptr]):
                    return False
                l_ptr+=1
                r_ptr-=1
            return True

        def dfs(index, cur_list):
            nonlocal return_list
            if(index>=len(s)):
                return_list.append(cur_list.copy())
                return
            
            for i in range(index, len(s)):
                cur_str=s[index:i+1]
                if(check(cur_str)):
                    cur_list.append(cur_str)
                    dfs(i+1, cur_list)
                    cur_list.pop()
            return
        dfs(0, [])
        return return_list
            
            