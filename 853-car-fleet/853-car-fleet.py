class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Idea is, some set of cars will reach together as fleet to the target.
        We need to find how many such cars are there.
        
        Logic is, we find the remaining time to reach destination. distance/speed formula.
        If something which can reach faster than the currently closest, we make it that much slow. And make reach as fleet.
        In the end number of such cars in the stack is the result. 
        """
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            # remaining time to reach, is more than the top of stack. Only then push it
            # else if it can reach faster than top of stack element, we ignore pushing to stack
            # and finally return the stack count as fleet. 
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)