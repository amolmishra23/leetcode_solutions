class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def solve(digits, index, curr, res):
            if index == len(digits):
                res.append(''.join(curr))
                return
            
            for char in num_to_letter[digits[index]]:
                curr.append(char)
                solve(digits, index+1, curr, res)
                curr.pop()
        
        if len(digits)==0: return []
        res = []
        solve(digits, 0, [], res)
        return res