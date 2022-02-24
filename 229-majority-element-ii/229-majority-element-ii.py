class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        n1, n2 = None, None
        c1, c2 = 0, 0
        
        for num in nums:
            if n1 is not None and n1==num: c1+=1
            elif n2 is not None and n2==num: c2+=1
            elif c1==0: n1, c1 = num, 1
            elif c2==0: n2, c2 = num, 1
            else: c1-=1; c2-=1
        
        res = []
        if n1 is not None and nums.count(n1)>(n//3): res.append(n1)
        if n2 is not None and nums.count(n2)>(n//3): res.append(n2)
        return res