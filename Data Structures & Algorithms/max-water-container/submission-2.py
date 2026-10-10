class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr=0
        right_ptr=len(heights) - 1
        answer=0
        while left_ptr<right_ptr:
            length=right_ptr-left_ptr
            height=min(heights[left_ptr], heights[right_ptr])
            water_body=length*height
            answer=max(water_body, answer)
            if(heights[left_ptr]<heights[right_ptr]):
                left_ptr=left_ptr+1
            else:
                right_ptr=right_ptr-1
        return answer