class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter()

        for i in reversed(range(len(nums))):
            counter[nums[i]]+=1
            if counter[nums[i]]>1:
                return (i+3)//3

        return 0