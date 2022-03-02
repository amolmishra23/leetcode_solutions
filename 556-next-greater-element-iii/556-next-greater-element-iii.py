class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        k, l = -1, 0
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                k = i
                break
        else:
            return -1
        
        print(k)
        for i in range(n-1, k, -1):
            if nums[i]>nums[k]:
                l = i
                break
        print(l)
        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
        print(nums)
        return nums
    
    def num_to_list(self, n):
        digits = []
        while n:
            digits.append(n%10)
            n //= 10
        digits.reverse()
        return digits
    
    def list_to_num(self, arr):
        res = 0
        for i in arr:
            res = res*10+i
        
        return res if (abs(res) <= (2**31)-1) else -1
    
    def nextGreaterElement(self, n: int) -> int:
        arr = self.num_to_list(n)
        res = self.nextPermutation(arr)
        return res if res==-1 else self.list_to_num(res)