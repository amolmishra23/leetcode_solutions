class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited, res = set(), 0
        
        for i in nums:
            # if we have not visited i before
            if i not in visited:
                curr = i
                count = 0
                while curr not in visited:
                    visited.add(curr)
                    curr = nums[curr]
                    count += 1
                # by now we have the count in "count", how long did we traverse
                res = max(res, count)
                
        return res