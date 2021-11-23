"""
EXPLANATION:-
Suppose array is [1, 1, 2, 2, 3, 3, 4, 5, 5]
we can observe that for each pair, 
first element takes even position and second element takes odd position
for example, 1 is appeared as a pair,
so it takes 0 and 1 positions. similarly for all the pairs also.

this pattern will be missed when single element is appeared in the array.

From these points, we can implement algorithm.
1. Take left and right pointers . 
    left points to start of list. right points to end of the list.
2. find mid.
    if mid is even, then it's duplicate should be in next index.
	or if mid is odd, then it's duplicate  should be in previous index.
	check these two conditions, 
	if any of the conditions is satisfied,
	then pattern is not missed, 
	so check in next half of the array. i.e, left = mid + 1
	if condition is not satisfied, then the pattern is missed.
	so, single number must be before mid.
	so, update end to mid.
3. At last return the nums[left]

Time: -  O(logN)
space:-  O(1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        
        # Performing the boundary checks
        if high==0: return nums[0]
        elif nums[low]!=nums[low+1]: return nums[low]
        elif nums[high]!=nums[high-1]: return nums[high]
        
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]: return nums[mid]
            
            if (mid%2==0 and nums[mid]==nums[mid+1]) or \
                (mid%2==1 and nums[mid]==nums[mid-1]):
                low = mid+1
            else:
                high = mid-1
                
        return -1