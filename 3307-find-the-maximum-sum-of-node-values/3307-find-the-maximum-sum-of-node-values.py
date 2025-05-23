class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        """
        https://www.youtube.com/watch?v=bnBp6_b4GCw
        Whole idea here is nums[i]^k=x
        nums[i]^x = k
        So we intend to find what we can maximize the array to
        all such edges (2 numbers) which xor will be more, we include them
        for the last element we check if xor is profitable, or not profitable.
        accordingly we return the result.
        """
        totalSum = 0
        count = 0
        positiveMin = float("inf")
        negativeMax = float("-inf")

        for nodeValue in nums:
            nodeValAfterOperation = nodeValue ^ k

            totalSum += nodeValue
            netChange = nodeValAfterOperation - nodeValue

            if netChange > 0:
                positiveMin = min(positiveMin, netChange)
                totalSum += netChange
                count += 1
            else:
                negativeMax = max(negativeMax, netChange)

        if count % 2 == 0:
            return totalSum
        return max(totalSum - positiveMin, totalSum + negativeMax)