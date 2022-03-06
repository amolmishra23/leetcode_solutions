class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        Result is basically for each puzzle, how many words match
        So we first convert each word to bitmask format (setting only bits which contain the characters)
        Then we generate all permutations of puzzle possible, again their bitmasks.
        Finally we see out of those permutations how many words do we have available
        And return the answer
        """
        count = Counter()
        
        for w in words:
            # if word contains more than 7 chars, no puzzle such exists, and we can ignore the word. 
            if len(set(w))>7: continue
                
            # generating the bitmask representation of the word, and saving in a counter. 
            mask = 0
            for c in set(w): 
                mask |= 1<<(ord(c)-97)
            count[mask] += 1
            
        res = []
        
        for p in puzzles:
            # first letter is mandatory to be there in the word
            bfs = [1<<(ord(p[0])-97)]
            
            # for remaining letters, we generate all the possible combinations
            for c in p[1:]:
                # everytime whatever available in bfs(by far), we try to set the bitmask at position c. 
                # this helps us generate all permutations like in dp (educative chapter 11)
                # same dp logic applies (TAKE ONE LEAVE ONE)
                bfs += [m | 1 << (ord(c)-97) for m in bfs]
            
            # whatever mask matches among all possible generated permutations through bfs
            res.append(sum(count[m] for m in bfs))
        
        return res
            
            