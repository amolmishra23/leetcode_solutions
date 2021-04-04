class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1, f2 = [], []
        
        for s in range(1, int(sqrt(n))+1):
            if n%s==0:
                f1.append(s)
                f2.append(n//s)
        
        if f1[-1]==f2[-1]: f2.pop()
            
        f1.extend(f2[::-1])
        
        return -1 if len(f1)<k else f1[k-1]