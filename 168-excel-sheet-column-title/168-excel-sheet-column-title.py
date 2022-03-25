class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def solve(num):
            return "" if num==0 else solve((num-1)//26)+string.ascii_uppercase[(num%26)-1]
        
        return solve(columnNumber)