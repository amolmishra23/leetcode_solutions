class Solution:
    def threeSumClosest(self, arr: List[int], target: int) -> int:
        arr.sort()
        min_diff, min_sum = float('inf'), 0

        for i in range(len(arr)-2):
            if i>0 and arr[i]==arr[i-1]: continue
            left, right = i+1, len(arr)-1
            while left<right:
                curr_sum = arr[i]+arr[left]+arr[right]
                if curr_sum == target: return curr_sum

                curr_diff = abs(curr_sum-target)

                if curr_diff<min_diff:
                    min_diff = curr_diff
                    min_sum = curr_sum

                if curr_sum>target: 
                    right-=1
                    while left<right and arr[right]==arr[right+1]: right-=1
                else: 
                    left+=1
                    while left<right and arr[left]==arr[left-1]: left+=1

        return min_sum
