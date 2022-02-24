class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        Very similar to how we solved ugly numbers-2. there we were moving pointers and deciding which is minimum
        Here to do that efficiently, as more number of primes, 
        we store all primes next smallest in heap, and choose from heap
        
        As we pop from heap, we also push next min most. Using same logic, dp[i]*t2/t3/t5. 
        Here which is stored in heap itself.
        """
        
        # smallest, original_prime, index_to_multiply in dp
        cand = [(p, p, 1) for p in primes]
        ugly = [1]
        
        for _ in range(n-1):
            ugly.append(cand[0][0])
            
            while cand[0][0] == ugly[-1]:
                ugly_num, prime, pos = heapq.heappop(cand)
                heapq.heappush(cand, (prime*ugly[pos], prime, pos+1))
                
        return ugly[-1]
            