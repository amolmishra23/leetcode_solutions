"""
nums = [1, 2, 4, 13, 43]. We go form the smallest number add them one by one and always keep the possible range of numbers we can get in the form [0, k], that is, it is not union of intervals, but only one interval. Let us go through this example.

We did not choose any numbers yet, so we have interval [0, 0].
Are we missing something if we take next number 1? No, let us take it, now we have interval [0, 1].
Are we missing something if we take next number 2? No, let us take it, now we have interval [0, 3].
Are we missing something if we take next number 4? No, let us take it, now we have interval [0, 7].
Are we missing something if we take next number 13? Yes, we missing! What we need to take next patch equal to 8. So now, our interval is [0, 15].
Our next missing number 16 is more, than next number in array: 13. So if fact, we can create [0, 28].
Our next missing number is 29, it is less than 43, so we add 29 as patch. and we have interval [0, 57].
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, max_reach = 0, 0
        i = 0
        
        while max_reach < n:
            # if we find such a number that its greater than our max_reach+1.
            # including it directly we may miss to generate some numbers in between
            # hence in such circumstances we need to perform the patching
            if i<len(nums) and nums[i]<=max_reach+1:
                max_reach += nums[i]; i+=1
            else:
                patches += 1
                max_reach += (max_reach + 1)
                
        return patches