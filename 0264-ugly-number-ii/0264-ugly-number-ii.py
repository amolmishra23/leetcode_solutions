class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<=0: return false
        if n==1: return 1
        
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        
        for _ in range(1, n):
            next_num = min(
                nums[i2]*2, nums[i3]*3, nums[i5]*5
            )
            nums.append(next_num)
            if next_num == nums[i2]*2:
                i2+=1
            if next_num == nums[i3]*3:
                i3+=1
            if next_num == nums[i5]*5:
                i5+=1
        
        return nums[n-1]
        
    def nthUglyNumber1(self, n: int) -> int:
        heap, seen = [1], set()
        
        for i in range(n):
            curr = heapq.heappop(heap)
            if i==n-1: return curr
            for j in [2,3,5]:
                if curr*j not in seen:
                    heapq.heappush(heap, curr*j)
                    seen.add(curr*j)
                    
        return