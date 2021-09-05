class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        We just need to check, if we can reach nth node, from any node in the world.
        To reach from ith node, we should have a budget greater than or equal to that node. 
        then we can form the dp recurrence relation to reach it. 
        """
        last_pos = len(nums)-1
        
        for i in range(len(nums)-2, -1, -1):
            if i+nums[i] >= last_pos: last_pos=i
                
        return last_pos==0