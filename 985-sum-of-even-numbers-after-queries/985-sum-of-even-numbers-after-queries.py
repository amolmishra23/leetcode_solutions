class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        summ = sum(a for a in A if a%2==0)
        
        for x, y in queries:
            if A[y]%2==0: summ-=A[y]
            A[y]+=x
            if A[y]%2==0: summ+=A[y]
            res.append(summ)
            
        return res