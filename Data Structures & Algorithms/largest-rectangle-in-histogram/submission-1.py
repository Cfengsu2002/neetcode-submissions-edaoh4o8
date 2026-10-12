class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start_index = i

            while stack and stack[-1][1] > height:
                prev_start, prev_height = stack.pop()
                max_area = max(
                    max_area,
                    prev_height * (i - prev_start)
                )
                start_index = prev_start
            stack.append((start_index, height))

        # 栈中剩下的高度可以一直延伸到数组末尾
        for start_index, height in stack:
            max_area = max(
                max_area,
                height * (len(heights) - start_index)
            )

        return max_area