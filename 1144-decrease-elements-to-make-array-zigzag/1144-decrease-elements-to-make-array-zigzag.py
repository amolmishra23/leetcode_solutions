class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        Very simple solution. 
        We can only decrease, to make array zig zag. 
        Either we go decreasing all even indexed elements, or decrease all odd indexed elements. 
        We calculate both the possibilites and in the end return min result. 
        """
        n, result = len(nums), [0,0]
        
        for i in range(n):
            left = nums[i-1] if i-1>=0 else float('inf')
            right = nums[i+1] if i+1<=n-1 else float('inf')
            result[i%2] += max(
                nums[i]-min(left, right)+1,
                0
            )
            
        return min(result)