class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt, ans, cum_sum = Counter(arr), 0, 0
        
        # to remove min elements, to make array half, we need to remove most freq elements first
        for freq in sorted(cnt.values(), reverse=True):
            # ans contains number of elements removed
            ans += 1
            cum_sum += freq
            # we can return as soon as we found, we removed half the elements
            if cum_sum >= len(arr)//2: return ans
        
        # worst case we have removed all the elements
        return ans
        