class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        answer = 0
        hash_map = {}

        for num in visited:
            checking_value = num
            count = 0  

            while checking_value in visited:
                if checking_value in hash_map:
                    count += hash_map[checking_value]
                    break

                checking_value -= 1
                count += 1

            answer = max(answer, count)
            hash_map[num] = count

        return answer