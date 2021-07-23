class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Very simple question to solve, just need to break at each point, until we are palindrome
        And record all the breaks, which can result as to palindrome formation
        For which most efficient way is to backtrack. 
        """
        def backtrack(start, end, tmp):
            if start==end:
                ans.append(tmp[:])
            
            for i in range(start, end):
                cur = s[start:i+1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(i+1, end, tmp)
                    tmp.pop()
                    
        ans = []
        backtrack(0, len(s), [])
        return ans