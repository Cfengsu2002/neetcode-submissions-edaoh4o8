class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        max_area=0
        for index, height in enumerate(heights):
            if(not stack):
                stack.append((index, height))
            else:
                prev_index=float('inf')
                while (stack and height<stack[-1][-1]):
                    prev_index, pre_height=stack.pop()
                    max_area=max(max_area,pre_height*(index-prev_index))
                stack.append((min(prev_index, index), height))
        for i, height in stack:
            max_area=max(max_area, (len(heights)-i)*height)
        return max_area