"""
Also can be solved optimally using a monotonic decreasing stack, as top element is always smallest element
So we use smallest element first, that it will be added maximum number of times, decrerasing total value as less as possible

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                cur = stack.pop()
                if stack:
                    res += cur * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

"""

class Solution:
    # Understandable solution: https://www.youtube.com/watch?v=pYs3qj42h3c&t=1338s
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.helper(arr, 0, len(arr) - 1, {})
        
    def helper(self, arr, l, r, cache):
        if (l, r) in cache:
            return cache[(l, r)]
        # we are at leaf node. So return 0
        if l >= r:
            return 0
        
        res = float('inf')
        # Concept of MCM pretty much
        for i in range(l, r):
            # value at room is, sum of max leaf nodes from left and righ subtrees. 
            rootVal = max(arr[l:i+1]) * max(arr[i+1:r+1])
            # then we recursively find the sum of new added nodes. And min most value is our result. 
            res = min(res, rootVal + self.helper(arr, l, i, cache) + self.helper(arr, i + 1, r, cache))
        
        cache[(l, r)] = res
        return res