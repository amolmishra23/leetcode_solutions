class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def compare(a, b):
            if a+b > b+a: return -1
            else: return 1
            
        nums.sort(key = cmp_to_key(compare))
        return str(int("".join(nums)))