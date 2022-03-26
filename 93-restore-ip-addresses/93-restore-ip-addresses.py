class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        def solve(idx, curr):
            if idx==n and len(curr)==4: 
                self.res.append(".".join(curr))
                return
            if idx==n or len(curr)==4:
                return 
            
            
            for curr_len in range(1, 4):
                if idx+curr_len > n: break
                
                curr_str = s[idx:idx+curr_len]
                
                if int(curr_str)>255 or (curr_len>1 and s[idx]=="0"): break
                
                curr.append(curr_str)
                solve(idx+curr_len, curr)
                curr.pop()
                
        self.res = []
        solve(0, [])
        return self.res