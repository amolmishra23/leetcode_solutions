class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        if less than 3 nums, anyways cant form a traingle.
        we do it using 2 pointer approach in gtci. 
        after sorting the input array, every possible pair, we see if their sum is bigger than 3rd number. If it is, then all numbers between them also form valid input. 
        2,2,3,4
        L=0, R=2, i=3 
        If L+R>ith element. Means all elements in between also form valid pairs, hence we add them to res.
        Then we reduce right, and increment left. 
        """
        if len(nums)<3: return 0
        
        res = 0
        nums.sort()
        
        for i in range(2, len(nums)):
            left, right = 0, i-1
            
            # doing it in 2 pointer approach
            # for curr i index fixed, find the left and right, such that their sum are bigger than nums[i]
            # then we keep shrinking window also accordingly. 
            while left<right:
                if nums[left]+nums[right]>nums[i]:
                    res += right-left
                    right-=1
                else:
                    left+=1
                    
        return res
        