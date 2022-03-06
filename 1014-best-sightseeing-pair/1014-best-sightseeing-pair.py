class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
        This is an extension of the kadane algorithm. 
        The formula given to us, A[i] + A[j] + i - j, we break it into 2 parts. 
        First we try to find, max possible with A[i]+i. 
        Then at each step, we try seeing, Adding which A[j]-j, reduces the result minimum so as to attain the max possible value. 
        """
        
        res, cur = 0, 0
        
        for i, x in enumerate(A):
            # curr = A[i]+i
            # other term is A[j]-j
            # we need to maximize the curr and minimize the 2nd term difference. 
            
            # another condition is i should come before j. 
            # to fulfill this, initially cur is 0, when res is 1st calculated. 
            # next iterations onwards we currently guess the values. 
            res = max(res, cur+x-i)
            cur = max(cur, i+x)
            
        return res