class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count, res = Counter(), 0

        for d in dominoes:
            k = min(d[0], d[1])*10 + max(d[0], d[1])
            count[k]+=1
        
        return sum((v*(v-1))//2 for v in count.values())