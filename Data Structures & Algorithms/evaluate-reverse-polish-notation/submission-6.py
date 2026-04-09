class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens.reverse()
        num_list = []

        while tokens:
            if tokens[-1] not in ['+', '-', '*', '/']:   # ✅ 改这里
                num_list.append(int(tokens[-1]))
            elif tokens[-1] == '+':
                num1 = num_list.pop()
                num2 = num_list.pop()
                num_list.append(num1 + num2)
            elif tokens[-1] == '*':
                num1 = num_list.pop()
                num2 = num_list.pop()
                num_list.append(num1 * num2)
            elif tokens[-1] == '-':
                num1 = num_list.pop()
                num2 = num_list.pop()
                num_list.append(num2 - num1)
            elif tokens[-1] == '/':
                num1 = num_list.pop()
                num2 = num_list.pop()
                num_list.append(int(num2 / num1))  # ✅ 改这里

            tokens.pop()

        return num_list[-1]