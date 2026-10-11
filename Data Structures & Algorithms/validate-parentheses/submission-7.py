class Solution:
    def isValid(self, s: str) -> bool:
        parenthese={')':'(', ']':'[', '}':'{'}
        stack=[]
        for i in range(len(s)):
            if s[i] not in parenthese:
                stack.append(s[i])
            elif(not stack or parenthese[s[i]]!=stack[-1]):
                return False
            else:
                stack.pop()
        return True if not stack else False