class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # curr is the branch
        # i is the number of elements traversed
        # https://www.youtube.com/watch?v=wRubz1zhVqk
        curr, i = 1,1

        def count(curr):
            # Assume n=100
            # curr=1, nei=2, we get 1 element here
            # curr=10, nei=20, we get 10 elements here
            # curr=100, nei=200, we get 100 elements here
            res, nei = 0, curr+1

            while curr<=n:
                res += min(nei, n+1)-curr
                curr*=10
                nei*=10

            return res

        while i<k:
            steps = count(curr)
            if i+steps <= k:
                # increment branch by 1
                curr = curr+1
                # increment i by number of steps 
                i+=steps
            else:
                # diving deeper in the branch
                curr *= 10
                # as we passed by current number, we add 1. 
                i+=1

        return curr

