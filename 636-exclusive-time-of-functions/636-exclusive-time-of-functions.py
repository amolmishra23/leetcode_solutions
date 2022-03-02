class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = []
        res = [0]*n
        prev = 0
        
        for log in logs:
            tokens = log.split(':')
            if tokens[1] == "start":
                if stk:
                    res[stk[-1]] += int(tokens[2]) - prev
                stk.append(int(tokens[0]))
                prev = int(tokens[2])
            else:
                res[stk.pop()] += int(tokens[2])-prev+1
                prev = int(tokens[2])+1
        
        return res