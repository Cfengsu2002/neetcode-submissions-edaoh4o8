class Solution:
    def partition(self, s: str) -> List[List[str]]:
        current_path = []
        answer = []

        def is_palindrome(text):
            l, r = 0, len(text) - 1
            while l < r:
                if text[l] != text[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(start_index):
            if start_index == len(s):
                answer.append(current_path.copy())
                return

            for end_index in range(start_index, len(s)):
                substring = s[start_index:end_index + 1]

                if not is_palindrome(substring):
                    continue

                current_path.append(substring)
                dfs(end_index + 1)
                current_path.pop()

        dfs(0)
        return answer