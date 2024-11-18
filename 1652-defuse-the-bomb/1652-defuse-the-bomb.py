class Solution:
    def solve(self, arr, k):
        n = len(arr)
        if n==0: return [0]*n
        
        k_sum = sum(arr[:k])
        res = []
        
        for i in range(n):
            k_sum -= arr[i]
            k_sum += arr[(i+k)%n]
            res.append(k_sum)
        
        return res
    
    def decrypt(self, code: List[int], k: int) -> List[int]:
        return self.solve(code, k) if k>=0 else list(reversed(self.solve(list(reversed(code)), -k)))
        
        
        