class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        n = len(rating)
        
        for i in range(1, n-1):
            curr = rating[i]
            
            left_small, left_large = 0, 0
            right_small, right_large = 0, 0
            
            for j in range(i):
                if rating[j]<rating[i]:
                    left_small += 1
                else:
                    left_large += 1
            
            for j in range(i+1, n):
                if rating[j]>rating[i]:
                    right_large += 1
                else:
                    right_small += 1
            
            res += left_small * right_large
            res += left_large * right_small
            
        return res