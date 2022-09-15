class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count, res = Counter(changed), []
        
        if len(changed)%2: return []
        
        for x in sorted(count):
            if count[x] > count[2*x]: return []
            
            if x==0:
                if count[x]%2: return []
                else: res.extend([0]*(count[x]//2))
            else:
                res.extend([x]*count[x])
            count[2*x]-=count[x]
            
        return res