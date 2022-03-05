class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total%3: return False
        
        target, accum, counter = total//3, 0, 0
        
        for x in A:
            if counter==2: return True       
            accum += x
            if accum==target:
                counter += 1
                accum = 0
        
        return False