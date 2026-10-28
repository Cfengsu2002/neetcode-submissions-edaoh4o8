class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_panlindrome(word):
            l=0
            r=len(word)-1
            while l<=r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        answer=[]
        def dfs(start_index, current_answer):
            nonlocal answer
            if current_answer:
                answer_sum=sum(len(value) for value in current_answer)
                if(answer_sum==len(s)):
                    answer.append(current_answer.copy())
            for i in range(start_index, len(s)):
                sub_answer=s[start_index:i+1]
                if is_panlindrome(sub_answer):
                    current_answer.append(sub_answer)
                    dfs(i+1, current_answer)
                    current_answer.pop()
        dfs(0, [])
        return answer
                