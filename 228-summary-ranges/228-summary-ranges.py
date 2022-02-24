class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        res = []
        if n==0: return []
        elif n==1: return list(map(str, nums))
        else:
            start, end = nums[0], nums[0]
            for i in range(1, n):
                if nums[i-1]+1==nums[i]:
                    end = nums[i]
                else:
                    if start==end:
                        res.append(f"{start}")
                    else:
                        res.append(f"{start}->{end}")
                    start, end = nums[i], nums[i]
            if start==end:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            start, end = nums[i], nums[i]
            return res