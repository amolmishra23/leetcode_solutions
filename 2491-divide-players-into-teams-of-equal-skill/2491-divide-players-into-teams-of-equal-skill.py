class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)%2: return -1
        target = sum(skill)//(len(skill)//2)
        
        count = Counter(skill)
        res = 0
        
        for x in skill:
            a, b = x, target-x
            if count[a]==0: continue
            if count[b]==0: return -1
            count[a]-=1; count[b]-=1
            res += (a*b)
            
        return res