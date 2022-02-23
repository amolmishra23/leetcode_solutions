class Solution:
    def grayCode(self, n: int) -> List[int]:
        """
        https://www.youtube.com/watch?v=Fha1CSxwvGg
        Logic is, for 2 bit binary numbers the sequence is 00,01,11,10. 
        Now if we need to generate 3 bit, we need to add 0 in front of it.
        But to maintain proper sequence, when we add 1, we add from the reverse end. 
        """
        def solve(n):
            if n==0: return ["0"]
            if n==1: return ["0", "1"]
            res = solve(n-1)
            return ["0"+s for s in res]+["1"+s for s in res[::-1]]
        return [int(s, 2) for s in solve(n)]