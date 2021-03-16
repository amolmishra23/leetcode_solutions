class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, n): fact.append(fact[-1]*i)
        
        k -= 1
        digits, res = [str(i) for i in range(1, n+1)], []
        
        while n:
            i, k = divmod(k, fact[n-1])
            res.append(digits.pop(i))
            n -= 1
            
        return ''.join(res)
        
        