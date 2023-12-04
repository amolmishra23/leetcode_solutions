class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i, res = 0, None
        
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]: 
                if not res or num[i]>res:
                    res = num[i]
                    
        return str(res)*3 if res is not None else ""