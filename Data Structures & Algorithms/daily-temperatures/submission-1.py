class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans_arr=[0]*len(temperatures)
        for i in range(len(temperatures)):
            current_temperature=temperatures[i]
            if(not stack):
                stack.append((current_temperature, i))
            else:
                while(stack and current_temperature>stack[-1][0]):
                    previous_temperature, previous_index=stack.pop()
                    ans_arr[previous_index]=i-previous_index
                else:
                    stack.append((current_temperature, i))
        return ans_arr