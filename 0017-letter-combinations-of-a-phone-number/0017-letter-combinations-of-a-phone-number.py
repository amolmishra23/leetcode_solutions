class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        res = []
        def solve(idx, curr):
            nonlocal res
            if idx == len(digits):
                res.append("".join(curr))
                return res
            
            for ch in self.map[digits[idx]]:
                curr.append(ch)
                solve(idx+1, curr)
                curr.pop()
                
        if len(digits)==0: return []
        solve(0, [])
        return res