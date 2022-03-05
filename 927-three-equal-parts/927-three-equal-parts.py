class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        """
        Logic to solve this problem is, If we need to divide orig number to 3 same numbers. 
        1. They need to have same number of 1s. 
        2. They should have 0s and 1s placed in same sequence. 
        
        So we use a 3 pointer technique. Find the location of 3 pointers, and move them keep checking if all numbers are same. 
        if there are 6 ones, the location is going to be like this [1,1,1,1,1,1] 0,2,4. Then keep moving 1 pointer at a time. 
        """
        
        ones = sum(a==1 for a in A)
        n = len(A)
        if ones==0: return [0, len(A)-1]
        if ones%3!=0: return [-1, -1]
        
        k = ones//3
        
        first, second, third = None, None, None
        
        for i in range(n):
            if A[i]==1: first=i; break
        
        gap_ones = k
        
        for i in range(first+1, n):
            if A[i]==1:
                gap_ones-=1
                if gap_ones==0: second=i; break
        
        gap_ones = k
        
        for i in range(second+1, n):
            if A[i]==1:
                gap_ones -= 1
                if gap_ones==0: third=i; break
        
        while third<n and A[first]==A[second]==A[third]:
            first+=1; second+=1; third+=1
        
        if third==n: return [first-1, second]
        return [-1, -1]
        
            