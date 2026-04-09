class Solution:

    def encode(self, strs: List[str]) -> str:
        code=""
        for element in strs:
            code=code+element+"好"
        return code
    def decode(self, s: str) -> List[str]:
        print(s)
        ans_list=s.split("好")
        print(ans_list)
        return ans_list[:-1]