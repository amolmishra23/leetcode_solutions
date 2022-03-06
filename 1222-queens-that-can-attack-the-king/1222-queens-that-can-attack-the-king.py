class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """
        Wherever king is placed, we go as deep as possible in each of the 8 directions. 
        If we find any queen, we increment res, and add that queen
        Finally we return res
        """
        
        dirs = [
            [-1,-1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        lookup, res = {(i, j) for i, j in queens}, []
        
        for dx, dy in dirs:
            for i in range(8):
                x, y = king[0]+dx*i, king[1]+dy*i
                if not 0<=x<8 or not 0<=y<8: break
                if (x, y) in lookup: res.append([x,y]); break
        
        return res