class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        Can be solved in multiple complex ways. 
        Binary search tree, segment tree etc
        But binary search seems to be easiest. Just go on inserting elements in the sorted order.
        And index which inserting, is the answer, as that many elements on left are smaller than this number. 
        """
        
        sorted_arr = []
        result = []
        
        for i in range(len(nums)-1, -1, -1):
            idx = bisect.bisect_left(sorted_arr, nums[i])
            result.append(idx)
            sorted_arr.insert(idx, nums[i])
            
        return result[::-1]