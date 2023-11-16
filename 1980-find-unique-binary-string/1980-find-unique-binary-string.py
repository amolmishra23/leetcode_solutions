class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        return "".join(["0" if ch[i]=="1" else "1" for i, ch in enumerate(nums)])