class Solution(object):
    """
    To create the max number from num1 and nums2 with k elements, we assume the final result combined by i numbers (denotes as left) from num1 and j numbers (denotes as right) from nums2, where i+j==k.

    Obviously, left and right must be the maximum possible number in num1 and num2 respectively. i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].

    The final result is the maximum possible merge of all left and right.

    So there're 3 steps:

    iterate i from 0 to k.
    find max number from num1, num2 by select i , k-i numbers, denotes as left, right
    find max merge of left, right
    function maxSingleNumber select i elements from num1 that is maximum. The idea find the max number one by one. i.e. assume nums [6,5,7,1,4,2], selects = 3.
    1st digit: find max digit in [6,5,7,1], the last two digits [4, 2] can not be selected at this moment.
    2nd digits: find max digit in [1,4], since we have already selects 7, we should consider elements after it, also, we should leave one element out.
    3rd digits: only one left [2], we select it. and function output [7,4,2]
    """
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = [0]*k
        m=len(nums1);n=len(nums2)
        for i in range(0,k+1):
            j=k-i
            if i>m or j>n:
                continue
            res1 = self.getMaxNumber(nums1, i)
            res2 = self.getMaxNumber(nums2, j)
            merged = self.MergeMaxNums(res1, res2,k)
            res = max(merged, res)
        return res
        
    def MergeMaxNums(self, n1, n2,nk):
        r = []
        while (n1 or n2) and nk>0:
            if n1>n2:
                r.append(n1[0])
                n1=n1[1:]
            else:
                r.append(n2[0])
                n2=n2[1:]
            nk-=1
        return r
        
    def getMaxNumber(self, nums, L):
        stack = []
        i=0
        while i<len(nums):
            remain = len(nums)-i
            while len(stack) and nums[i]>stack[-1] and L<remain:
                L+=1
                stack.pop()
            L-=1
            stack.append(nums[i])
            i+=1
        return stack