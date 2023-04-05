class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        """
        Assume we are given 1,5,10
        As per problem everytime we increase idx, and reduce idx-1
        So, the sum remains same. 
        So we will now have 3,3,10. (4,9,5,8,6,7)
        Next we will have 3,6,7
        We can even make it 4,5,7. And then (4,6,6)
        
        Finally our res is 6 now. This also could very simply be computed as 1+5+10//3 = 16//3 = 5+1 => 6
        This needs to be done at every step. 
        """
        max_val, curr_sum = 0, 0
        
        for i, num in enumerate(nums, 1):
            curr_sum += num
            q, r = divmod(curr_sum, i)
            if r: q+=1
            max_val = max(max_val, q)
        
        return max_val