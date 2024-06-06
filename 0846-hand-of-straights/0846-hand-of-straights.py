class Solution:
    def isNStraightHand(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        
        for i in sorted(count):
            if count[i]<=0: continue
            required = count[i]
            for j in range(i, i+k):
                if count[j]<required: return False
                count[j]-=required
        
        return True