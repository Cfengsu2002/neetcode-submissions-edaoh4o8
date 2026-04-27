class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_cha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        return_list=[]
        def dfs(cur_cha="", cur_index=0):
            nonlocal return_list
            if(len(cur_cha)==len(digits)):
                return_list.append(cur_cha)
                return
            cur_num=digits[cur_index]
            for element in num_to_cha[cur_num]:
                cur_cha=cur_cha+element
                dfs(cur_cha, cur_index+1)
                cur_cha=cur_cha[:-1]
            return
        dfs()
        return return_list if len(digits)!=0 else []


