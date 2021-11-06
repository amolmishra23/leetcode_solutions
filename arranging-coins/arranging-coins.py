class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        We need to correctly find the value of k(number of full rows), while accomodating n coins.
        Now sequentially we can do in O(n) without much trouble
        In order to make it O(logn), we can retort to binary search
        
        Everytime make a guess for k. And find number of coins, in k rows.
        If that number of coins is less than n, our answer is in right sub-array. Else in left-subarray
        Eventually if we get equal, that is our k. (most optimal)
        Else if we get out of loop, left>right. So answer is right(as those rows were surely complete)
        """
        left, right = 0, n
        
        while left<=right:
            mid = left + (right-left)//2 # this is for k
            curr = mid * (mid+1)//2 # number of coins in k rows. Simple n*(n+1)//2 formula.
            
            # conditions applied
            if curr==n: return mid
            elif curr<n: left = mid+1
            else: right = mid-1
        
        # returning number of full rows. 
        return right
            