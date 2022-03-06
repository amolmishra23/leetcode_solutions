class Solution:
    
    def __init__(self):
        self.func_table = dict()
        
        # base case:
        self.func_table[0] = 0
        self.func_table[1] = 1
        self.func_table[2] = 1
        
    
    def tribonacci(self, n: int) -> int:
        
        if n in self.func_table:
            # qucik resonse if tribonacci(n) has been computed before
            return self.func_table[n]
        
        else:
            # recusrion with memorization 
            self.func_table[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)
            return self.func_table[n]