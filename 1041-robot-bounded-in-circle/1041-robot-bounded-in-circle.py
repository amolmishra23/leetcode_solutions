class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        1. the robot is already back to its origin by the end of the string traversal, and
        2. the robot is away from the origin, but heading to a direction different from its initial direction. For example, if the robot is facing left by the end of the first string traversal, after three other traversals of left->left->left, it is back to the origin. A second example is that if the robot is facing down by the end of the first string traversal, it only takes another traversal for it to get back to the origin.
        """
        di = (0,1)
        x, y = 0, 0
        
        for ins in instructions:
            if ins=="G":
                x, y = x+di[0], y+di[1]
            elif ins=="L":
                di = (-di[1], di[0])
            elif ins=="R":
                di = (di[1], -di[0])
                
        return (x==0 and y==0) or di!=(0,1)