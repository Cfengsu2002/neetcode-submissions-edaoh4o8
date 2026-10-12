class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=deque()
        tokens=deque(tokens)
        while tokens:
            token=tokens.popleft()
            if(token not in ('+', '-', '*', '/')):
                stack.append(token)
            else:
                first_value=int(stack.pop())
                second_value=int(stack.pop())
                if(token=='+'):
                    stack.append(str(first_value+second_value))
                if(token=='/'):
                    added_value=str(int(second_value/first_value))
                    stack.append(added_value)
                if(token=='*'):
                    stack.append(str(first_value*second_value))
                if(token=='-'):
                    stack.append(str(second_value-first_value))
        return int(stack[0])
