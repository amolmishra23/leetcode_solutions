class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        This is an extremely tricky question. https://www.youtube.com/watch?v=Dxv_kCAYOk4&t=5s
        Lets say we are into 1-3-2, we can make it 1-2-2. Or we can make it 1-3-3. 
        First pref is if (i-2)<i, then we make it 1-2-2
        If our number was 3-4-2, then we have no choice but to make as 3-4-4. We cant make it 3-2-2 because balance is disturbed
        """
        if len(nums)<=1: return True
        isPossible = False
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                if count>0: return False
                if i==1 or nums[i-2]<=nums[i]:
                    # First pref is if (i-2)<i, then we make it 1-2-2
                    nums[i-1] = nums[i]
                else:
                    # 3-4-2, then we have no choice but to make as 3-4-4
                    nums[i] = nums[i-1]
                count+=1
        
        return True