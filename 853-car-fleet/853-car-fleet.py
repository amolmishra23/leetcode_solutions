class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        
        for pos, speed in sorted(zip(position, speed))[::-1]:
            dist = target-pos
            rem_time = dist/speed
            if not stk:
                stk.append(rem_time)
            elif stk[-1]<rem_time:
                stk.append(rem_time)
            else:
                continue
                
        return len(stk)