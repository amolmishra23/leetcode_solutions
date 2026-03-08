class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums = set(nums)

        def backtrack(i, curr):
            if i==n:
                return "".join(curr) if "".join(curr) not in nums else ""
                
            for ch in ["0", "1"]:
                res = backtrack(i+1, curr+[ch])
                if len(res)!=0: return res

            return ""

        return backtrack(0, [])
