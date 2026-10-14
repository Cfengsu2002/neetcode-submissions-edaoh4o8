class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper_ptr = 0
        lower_ptr = len(matrix) - 1

        # 找到第一行：该行最后一个元素 >= target
        while upper_ptr < lower_ptr:
            middle_row = (upper_ptr + lower_ptr) // 2

            if matrix[middle_row][-1] < target:
                upper_ptr = middle_row + 1
            else:
                lower_ptr = middle_row

        answer_row = upper_ptr

        left_ptr = 0
        right_ptr = len(matrix[answer_row]) - 1

        # 在这一行中找 target
        while left_ptr < right_ptr:
            middle_ptr = (left_ptr + right_ptr) // 2

            if matrix[answer_row][middle_ptr] == target:
                return True
            elif matrix[answer_row][middle_ptr] > target:
                right_ptr = middle_ptr
            else:
                left_ptr = middle_ptr + 1

        # 检查最后剩下的元素
        return matrix[answer_row][left_ptr] == target