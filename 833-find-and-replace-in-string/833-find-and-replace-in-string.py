class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n, k = len(s), len(indices)
        ans = [x for x in s]
        
        for i in range(k):
            idx, src = indices[i], sources[i]
            
            if idx+len(src)<=n and s[idx:idx+len(src)]==src:
                ans[idx] = targets[i]
                for j in range(idx+1, idx+len(src)):
                    ans[j]=""
                    
        return "".join(ans)
        