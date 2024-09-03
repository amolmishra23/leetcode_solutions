class Solution:
    def num_to_list(self, n):
        stk = []
        
        while n:
            n,r = divmod(n, 10)
            stk.append(r)
        
        return stk[::-1]
        
    
    def getLucky(self, s: str, k: int) -> int:
        t = [num for ch in s for num in self.num_to_list(ord(ch) - ord('a') + 1)]
        
        for _ in range(k-1): t = self.num_to_list(sum(t))
            
        return sum(t)
            
        