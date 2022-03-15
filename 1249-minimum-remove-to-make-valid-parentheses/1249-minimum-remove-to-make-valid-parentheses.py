class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ip, op_count = list(s), 0
        res = []
        
        for i, ch in enumerate(ip):
            if ch=="(": 
                op_count += 1
            elif ch==")":
                if not op_count: continue
                op_count -= 1
            res.append(ch)
        
        ip = []
        for i in range(len(res)-1, -1, -1):
            if res[i]=="(" and op_count:
                op_count-=1
                continue
            ip.append(res[i])
            
        return "".join(ip[::-1])