class MinStack:

    def __init__(self):
        self.min_stack=[]
        self.normal_stack=[]

    def push(self, val: int) -> None:
        if(len(self.min_stack)==0 or val<=self.min_stack[-1]):
            self.min_stack.append(val)
        self.normal_stack.append(val)
    def pop(self) -> None:
        if not self.normal_stack:
            print()

        elif (len(self.min_stack)!=0 and self.normal_stack[-1]==self.min_stack[-1]):
            self.min_stack.pop()
        self.normal_stack.pop()

    def top(self) -> int:
        if not self.normal_stack:
            print()
        else:
            return self.normal_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]