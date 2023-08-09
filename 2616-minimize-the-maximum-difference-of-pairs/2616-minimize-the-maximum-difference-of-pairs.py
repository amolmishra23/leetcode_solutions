class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p==0: return 0
        
        # sorting as we will easily find the least diff elements. 
        nums.sort()
        
        def isValid(threshold):
            res, i = 0, 1
            # greedy approach works here. 
            # example of a,b,c,d
            # We can choose a,b or b,c. 
            # but choosing a,b is better. Because c,d could still be an option this way
            while i<len(nums):
                if nums[i]-nums[i-1]<=threshold:
                    res += 1
                    i += 2
                else:
                    i += 1
                    
            # we need atleast p pairs. So anything equal or more is valid
            return res>=p
        
        l, r = 0, nums[-1]-nums[0]
        
        while l<r:
            m = l+(r-l)//2
            
            if isValid(m):
                r = m
            else:
                l = m+1
                
        return l