class Solution:
    def isValid(self, s: str) -> bool:
        stack_simulator=[]
        for i in range(len(s)):
            if(s[i]=='{' or s[i]=='(' or s[i]=='['):
                stack_simulator.append(s[i])
            else:
                if(len(stack_simulator)==0):
                    return False
                if(s[i]==')' and stack_simulator[-1]=='('):
                    stack_simulator.pop()
                elif(s[i]==']' and stack_simulator[-1]=='['):
                    stack_simulator.pop()
                elif(s[i]=='}' and stack_simulator[-1]=='{'):
                    stack_simulator.pop()
                else:
                    return False
        return True if len(stack_simulator)==0 else False 