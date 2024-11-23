class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        
        for r in range(m):
            i = n-1
            for c in range(n-1, -1, -1):
                if box[r][c]=="#":
                    box[r][c], box[r][i] = box[r][i], box[r][c]
                    i -= 1
                elif box[r][c]=="*":
                    i = c-1
                    
        res = []
        
        for c in range(n):
            col = []
            for r in range(m-1, -1, -1):
                col.append(box[r][c])
            res.append(col)
            
        return res