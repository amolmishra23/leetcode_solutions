import collections
import itertools

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        count = collections.Counter(A)
        result = 0
        
        for i, j in itertools.combinations_with_replacement(count, 2):
            k = target-i-j
            
            if i==j==k: result+=count[i]*(count[i]-1)*(count[i]-2)//6
            elif i==j!=k: result += count[i]*(count[i]-1)//2 * count[k]
            elif max(i, j)<k: result += count[i]*count[j]*count[k]
        
        return result % (10**9 + 7)