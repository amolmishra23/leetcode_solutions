class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        conv = {x:i for i,x in enumerate(mapping)}
        
        candidates = []
        for i, n in enumerate(nums):        
            mapped_n, base = 0, 1
            if n==0:
                mapped_n = mapping[n]
                
            while n>0:
                n, r = divmod(n, 10)
                mapped_n += (base*mapping[r])
                base *= 10
            candidates.append((mapped_n, i))
            
        candidates.sort()
        
        return [nums[i] for mapped, i in candidates]
        