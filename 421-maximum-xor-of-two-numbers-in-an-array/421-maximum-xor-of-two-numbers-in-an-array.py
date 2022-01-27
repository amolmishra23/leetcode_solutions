class Solution:
    def __init__(self):
        self.root = {}
        
    def insert_bits(self, num):
        # populating bit by bit, in the trie/ 
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        for x in bit_num:
            if x not in node: node[x]={}
            node = node[x]
    
    def find_max_xor(self, num):
        bit_num = bin(num)[2:].zfill(32)
        node = self.root
        res = ""
        
        for x in bit_num:
            target = "1" if x=="0" else "0"
            if target in node:
                # adding the opposite variable for most optimal xor. 
                res += target
                node = node[target]
            else:
                # adding the current variable itself
                res += x
                node = node[x]
        
        # best possible opposite digits num we found
        return int(res, 2)^num
        
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert_bits(num)
            
        res = 0
        for num in nums:
            res = max(res, self.find_max_xor(num))
            
        return res