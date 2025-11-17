class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, n in enumerate(nums):
            if n==1:
                if last is not None and i-last-1<k: return False
                last = i

        return True

