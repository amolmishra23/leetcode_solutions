class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        """
        [2,1,3,5,4]
        The logic is that, if 5th bulb(no 5) is maximum
        And this is the 5th bulb(index 4 is basically 5th bulb) we are processing, means that all 5 bulbs before 5 are there. Else blue becoming logic
        Number of times this blue becoming logic happens, is our result. 
        """
        result, right = 0, 0
        
        for i, num in enumerate(light, 1):
            right = max(num, right)
            result += (right==i)
        
        return result