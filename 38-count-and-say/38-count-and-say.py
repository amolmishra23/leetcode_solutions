class Solution:
    def countAndSay(self, n: int) -> str:
        """
        1 => 1
        2 => 11
        3 => 21
        4 => 1211
        
        To get the term for 4, we read the previous term 3.
        And go adding number of elements from previous term. 
        As we had 21. Means one 2, and one 1.
        Hence the result is 1211
        """
        def solve(seq):
            i, new_seq = 0, []
            while i<len(seq):
                count = 1
                while i<len(seq)-1 and seq[i]==seq[i+1]:
                    count += 1
                    i += 1
                new_seq.extend([str(count), seq[i]])
                i+=1
            return new_seq
            
        seq=["1"]
        for i in range(n-1):
            seq = solve(seq)
        return "".join(seq)