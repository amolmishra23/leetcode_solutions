class CombinationIterator:
    def helper(self, n, cl):
        # idea is to generate every binary number, containing cl number of 1s.
        # as they are one of the valid combinations
        
        # finding the last number. Lets say if 3 digit characters, 111 is last.
        # we iterate from 111 to 000, and find all binary num's which have 2 1's in them. 110, 101, 011
        end = int("1"*n, 2)
        ans = []
        
        for i in range(end+1):
            b = bin(i)[2:]
            # we zfill to n chars, because while generating combinations, it becomes easier
            # matching index to index, and generate the positions with 1. 
            if b.count("1") == cl: ans.append(b.zfill(n))
                
        return ans
        
    
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.n, self.cl = len(self.chars), combinationLength
        # caching all the combinations in binary form
        self.combinations = self.helper(self.n, self.cl)
        self.ind = len(self.combinations)-1

    def next(self) -> str:
        res = ""
        
        # picking the next valid combination
        # and filling all positions with characters, which contain 1st respectively
        for i in range(self.n):
            if self.combinations[self.ind][i]=="1":
                res += self.chars[i]

        self.ind -= 1
        return res

    def hasNext(self) -> bool:
        return self.ind > -1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()