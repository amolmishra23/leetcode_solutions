class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0]*n
        stk = []
        prev = None
        
        for log in logs:
            a,b,c = log.split(":")
            a,c = int(a),int(c)
            
            if b=="start":
                if stk:
                    res[stk[-1]] += c-prev
                stk.append(a)
                prev = c
            else:
                res[stk.pop()] += c-prev+1
                prev = c+1
                
        return res 