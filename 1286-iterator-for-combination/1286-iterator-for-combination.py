# class CombinationIterator:

#     def __init__(self, characters: str, combinationLength: int):
#         self.combinations = []
#         n, k = len(characters), combinationLength
        
#         def backtrack(first = 0, curr = []):
#             if len(curr) == k:
#                 self.combinations.append("".join(curr[:]))
#                 return
            
#             for i in range(first, n):
#                 curr.append(characters[i])
#                 backtrack(i+1, curr)
#                 curr.pop()
        
#         backtrack()
#         self.combinations.reverse()

#     def next(self) -> str:
#         return self.combinations.pop()

#     def hasNext(self) -> bool:
#         return bool(self.combinations)

class CombinationIterator:

    def gen_comb(self):
        end = int("1"*self.n, 2)
        res = []
        
        for i in range(end+1):
            b = bin(i)[2:]
            if b.count("1") == self.k:
                res.append(b.zfill(self.n))
                
        return res
        
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n, self.k = len(self.chars), combinationLength
        self.comb = self.gen_comb()
        self.ind = len(self.comb) - 1

    def next(self) -> str:
        s = ""
        for i in range(self.n):
            if self.comb[self.ind][i]!="0": s+= self.chars[i]
                
        self.ind -= 1
        return s

    def hasNext(self) -> bool:
        return self.ind > -1
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()