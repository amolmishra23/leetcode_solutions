class Solution:
    def jump(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        next_max, res = 0, 0
        
        """
        We keep running 2 parallel pointers. 
        We try to make a jump (need to find which is the max sized jump we can make)
        In the end we return which is the number of jumps we make
        This we do, as long as we didnt reach the last element. 
        """
            
        while fast<len(nums)-1:
            while slow<=fast:
                next_max = max(next_max, slow+nums[slow])
                slow += 1
            res += 1
            fast = next_max
            
        return res