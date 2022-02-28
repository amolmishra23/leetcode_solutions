class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        We keep a counter of which elem has maximum freq, and when it occured first. 
        To get shortest subarray, we need to have all elements, which cause the maximum freq. 
        So the answer is last_occurence-first_occurence+1
        Tricky case if max degree is same for 2 elements, we return minimum most possible. 
        """
        num_counts, first_seen = {}, {}
        degree, min_length = 0, 0
        
        for i, num in enumerate(nums):
            if not num in first_seen: 
                first_seen[num]=i
                num_counts[num]=1
            else:
                num_counts[num]+=1
            if num_counts[num]>degree:
                degree = num_counts[num]
                min_length = i-first_seen[num]+1
            elif num_counts[num]==degree:
                min_length = min(min_length, i-first_seen[num]+1)
        
        return min_length