class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        arr = [3,1,4,2]
        prefix_min = [3,1,1,1]
        Watch this video for more explanation: https://www.youtube.com/watch?v=xV-QDXn9Brc
        Or this post: https://leetcode.com/problems/132-pattern/discuss/906876/Python-O(n)-solution-with-decreasing-stack-explained
        
        Same logic of nearest smallest element. Stack we will be have is a dcreasing one [20,11,9,3...]
        if we need to traverse to the right(from jth to nth positions) and find the kth value, we rather keep caching the values in a stack.
        Order and sorting of elements isnt important. 
        
        1. min_list is the list, for choosing ith element
        2. whatever we iterate from right to left if for jth element
        3. now we also need to find kth element. which will be bigger than i, but smaller than j. 
        
        
        In stack, we keep popping the elements smaller than min_most element. Which is in our min_list array. As they are of no use.
        Because the ith value is fixed to be the one from min_list
        Now its for sure, topmost if there is an element, its bigger than value of i. 
        
        Now need to see, if our j is bigger than stk[-1]. If yes, we found our answer and return True.
        Else return False
        """
        if len(nums)<3: return False
        
        min_list = [None]*len(nums)
        min_list[0] = nums[0]
        
        for i in range(1, len(nums)):
            min_list[i] = min(min_list[i-1], nums[i-1])
            
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])           
        return False