class Solution:
    def countAndSay(self, n: int) -> str:
        def solve(seq):
            i, new_seq = 0, []
            
            while i<len(seq):
                count = 1
                while i<len(seq)-1 and seq[i]==seq[i+1]:
                    i+=1
                    count+=1
                new_seq.extend([str(count), seq[i]])
                i+=1
                
            return new_seq
        
        seq = ["1"]
        for i in range(n-1):
            seq = solve(seq)
        
        return "".join(seq)