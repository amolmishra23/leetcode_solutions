class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        cand = [(p, p, 1) for p in primes]
        ugly = [1]
        
        for _ in range(n-1):
            ugly.append(cand[0][0])
            
            while cand[0][0] == ugly[-1]:
                ugly_num, prime, pos = heapq.heappop(cand)
                heapq.heappush(cand, (prime*ugly[pos], prime, pos+1))
                
        return ugly[-1]
            