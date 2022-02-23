class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def solve(s, curr, res, idx, segments):
            if idx == len(s) and segments==4: res.append(".".join(curr)); return
            elif idx == len(s) or segments==4: return 
            
            for curr_len in range(1, 4):
                if idx+curr_len>len(s): break
                
                str_val = s[idx:idx+curr_len]
                val = int(str_val)
                
                if val>255 or (curr_len>=2 and str_val[0]=="0"): break
                
                curr.append(str_val)
                solve(s, curr, res, idx+curr_len, segments+1)
                curr.pop()
                
        
        res = []
        solve(s, [], res, 0, 0)
        return res
        