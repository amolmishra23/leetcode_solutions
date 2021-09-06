class Solution:
    def slowestKey(self, releaseTimes: List[int], keyPressed: str) -> str:
        max_time, res_key = releaseTimes[0], keyPressed[0]
        
        for i in range(1, len(releaseTimes)):
            curr_time = releaseTimes[i]-releaseTimes[i-1]
            if curr_time > max_time:
                max_time = curr_time
                res_key = keyPressed[i]
            elif curr_time==max_time:
                res_key = max(res_key, keyPressed[i])
                
        return res_key