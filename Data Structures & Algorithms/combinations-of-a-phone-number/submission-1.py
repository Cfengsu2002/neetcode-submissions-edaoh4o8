class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = [""]
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        current_answer=""
        answer=[]
        def dfs(number_index=0):
            nonlocal current_answer, answer
            if(len(current_answer)==len(digits)):
                answer.append(current_answer)
                return
            for first_letter in digitToChar[digits[number_index]]:
                current_answer=current_answer+first_letter
                dfs(number_index+1)
                current_answer=current_answer[:-1]
            return
        dfs()
        return answer