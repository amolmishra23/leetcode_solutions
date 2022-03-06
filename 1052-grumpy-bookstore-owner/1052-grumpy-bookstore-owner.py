class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        """
        This is an extension to the sliding window problem
        """
        
        curr_satisfied, n = 0, len(customers)
        
        for c, g in zip(customers, grumpy):
            curr_satisfied += c if g==0 else 0
        
        start = 0
        curr_sum, max_sum = 0, 0
        
        for i in range(n):
            # only add the customers in grumpy hours.
            # other hours anyways is included in the curr_sum
            if grumpy[i]: curr_sum+=customers[i]
            
            # finding the max_sum keeping the owner non grumpy for continuous X minutes
            if i-start+1>=X:
                max_sum = max(max_sum, curr_sum)
                if grumpy[start]: curr_sum-=customers[start]
                start+=1
        
        return curr_satisfied+max_sum