class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dict_ = defaultdict(int)
        
        for x in range(lowLimit, highLimit+1):
            dict_[sum([int(y) for y in str(x)])] += 1
            
        return max(dict_.values())