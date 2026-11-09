class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[] #[7, 9]
        intervals.sort()
        for i in range(len(intervals)):
            current=intervals[i] #[1, 5],
            if(len(stack)==0):
                stack.append(current) #[1, 5]
                continue
            while stack:
             #[1, 5]
                if stack[-1][1]>=current[0]: #[1,5]>=[6,9]
                    current[0]=min(stack[-1][0], current[0])
                    current[1]=max(stack[-1][1], current[1])
                    stack.pop()
                    if not stack:
                        stack.append(current)
                        break
                else:
                    stack.append(current)
                    break
        return stack
                