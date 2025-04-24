class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n, count = len(nums), len(set(nums))
        currCount, res, i = Counter(), 0, 0

        for j in range(n):
            currCount[nums[j]] += 1
            while len(currCount)==count:
                res += (n - j)
                currCount[nums[i]]-=1
                if currCount[nums[i]]==0:
                    del currCount[nums[i]]
                i+=1

        return res