class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counter = Counter(nums)
        
        def solve(curr):
            if len(curr)==len(nums):
                result.append(curr)
                return 
            
            for key in counter:
                if counter[key]:
                    counter[key]-=1
                    solve(curr + [key])
                    counter[key]+=1
        
        solve([])
        return result