class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9+7
        nums = [0]*26
        for ch in s:
            nums[ord(ch) - 97] += 1

        for _ in range(t):
            curr = [0]*26
            
            for j in range(25):
                v = nums[j]
                if v:
                    curr[j+1] = (curr[j+1]+v)%mod
            
            z = nums[25]

            if z:
                curr[0] = (curr[0]+z)%mod
                curr[1] = (curr[1]+z)%mod
            
            nums = curr

        res = 0
        for v in nums:
            res = (res+v)%mod

        return res
