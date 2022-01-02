class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        The idea is that, if we have number 100, we need 20 more to make it divisible by 60. 
        So, that can be found out by -100%60=20 because 100%60=40
        Then we find how many 20s in the array, and keep adding it to the result. As it can form as many pairs with as many 20s. 
        Finally return the result. 
        
        """
        res, counter = 0, collections.Counter()
        
        for i in time:
            # finding out occurences of remainder to make it divisible by 60
            res += counter[-i%60]
            
            # caching count of remainder of the current number
            # lets say 30 occured. We cache 30. 
            # now when 150 comes. -150%60=> 30. We already have 30. Hence we can add 1 to our result! 
            counter[i%60]+=1
        
        
        return res