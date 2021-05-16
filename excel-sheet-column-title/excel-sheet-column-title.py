class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {i:c for i, c in enumerate(string.ascii_uppercase)}
        
        q,res = columnNumber,deque()
        
        while q:
            temp = (q-1)%26
            res.appendleft(dic[temp])
            q = (q-1)//26
        
        return "".join(res)