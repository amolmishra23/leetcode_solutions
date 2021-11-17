class Solution:
    """
    This problem could be divided into 2 sub-problems:

    function getMax(nums, t):
    get t numbers from list nums to form one single maximized sub-list, with relative orders preserved

    function merge(nums1, nums2):
    merge nums1 and nums2 to form one single maximized list, with relative orders preserved

    The final result could be solved by enumerate the length of sub-list nums1 and nums2, and record the max merged list.
    """
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        ret = [0]*k
        
        for i in range(0, k+1):
            j = k-i
            if i>m or j>n: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        
        return ret
    
    def mergeMax(self, nums1, nums2):
        ans = []
        
        while nums1 or nums2:
            if nums1>nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        
        return ans
    
    def maxSingleNumber(self, nums, t):
        n = len(nums)
        ans = []
        
        for x in range(n):
            """
            you are agree that if we get any greater value than the value currently present in stack then we will pop the element i.e. ans[-1] < nums[k]
let's say ans = [1,2,3,4,5] and now we got nums[k] = 9 then we want to push 9 somewhere in the ans array but we have one constraint of len of size "t" so we are checking if we will pop the element from answer and after that if in future we have sufficient element to create "ans" of length "t".
And that is handle by the condition len(ans) + size - x > t
            """
            while ans and len(ans) + (n-x) > t and ans[-1]<nums[x]:
                ans.pop()
            if len(ans)<t: 
                ans += nums[x],
        
        return ans