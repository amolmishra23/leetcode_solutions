class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        Whole logic is that, in total we can update 3 numbers to whatever we like
        if we sort the array, and update the last 3 numbers, our answer is a[0]-a[-4]
        Else if first 1, last 2 numbers, ans is a[1]-a[-3]
        else is a[2]-a[-2]
        else is a[3]-a[-1]
        
        Same is achieved via heapq.nlargest as we dont need to sort entire array, but just need the prefix and suffix
        """
        if len(nums)<=4: return 0
        
        return min(a-b for a,b in zip(heapq.nlargest(4, nums), heapq.nsmallest(4, nums)[::-1]))
        