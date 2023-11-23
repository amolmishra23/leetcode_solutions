class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(l, r):
            mn, mx = min(nums[l:r+1]), max(nums[l:r+1])
            if (mx-mn)%(r-l)!=0: return False
            d = (mx-mn)//(r-l)
            return (d==0 and mx==mn) or all((x in set(nums[l:r+1])) for x in range(mn, mx, d))
        
        return [check(lq, rq) for lq,rq in zip(l,r)]