class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        k = 0
        
        for x in arr:
            if x%2==1:
                k += 1
            else:
                k = 0
                
            if k==3: return True
            
        return False