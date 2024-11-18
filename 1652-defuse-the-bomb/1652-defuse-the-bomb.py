class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0: return [0]*len(code)
        swap = False
        
        if k<0: code=code[::-1]; k=-k; swap=True
        code.extend(code[:k])
        
        curr_sum, res = 0, []
        
        for end in range(len(code)):
            curr_sum += code[end]
            if end>=k-1:
                res.append(curr_sum)
                curr_sum -= code[end-k+1]
                
        return res[1:][::-1] if swap else res[1:] 
                
                