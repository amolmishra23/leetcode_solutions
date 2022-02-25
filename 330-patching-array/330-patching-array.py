class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        """
        The goal of problem is to have min elements in nums array, such that we can generate any number between 1..n
        Best case, we dont add anything, and can generate anything till n.
        If we dont have an element, we need to add it to array.
        Example: 1,3
        We cant generate 2. So add 2. 
        As soon as we added 2, our reach is increased to 1+2 = 3
        After we add 3, our reach is increased to 6. Because 3+old_reach(3)=6
        """
        count, reach, i = 0, 0, 0
        
        # if our reach is less than n
        while reach<n:
            if i>=n:
                # we already exhausted our given array, so keep adding the lowest num possible, (reach+1).
                # our new reach kind of doubles now. 
                # as we are patching here, increase count by 1. 
                reach += (reach+1)
                count += 1
            elif i<len(nums) and nums[i]<=(reach+1):
                # if the num we are traversing, is less than reach, we are good to use it and increase reach
                # as no patching here, we dont increase the count by 1. 
                reach += nums[i]
                i+=1
                # if the num we are traversing, is more than reach
                # we need the missing numbers in between (reach+1). So add this number and patch array.
                # as we patch, we increase the count by 1. 
            else:
                reach += (reach+1)
                count+=1
                
                
        return count