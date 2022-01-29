class Solution:
    def nsr(self, arr):
        # stk contains the index of elements which could be potential solutions (strictly decreasing elements). 
        # top of stack contains biggest element. As we go deeper, we found more and more smaller elements. Potential solutions. 
        # res also contains indexes only. 
        n, res, stk = len(arr), [None]*len(arr), []

        for i in range(n-1, -1, -1):
            # stk is empty means no smaller elements on right
            if not stk:
                res[i] = n
            # we found the smallest closest element on the right
            elif arr[stk[-1]]<arr[i]:
                res[i] = stk[-1]
            else:
                # remove all the elements bigger than curr element
                # as they arent relevant anymore, after we have a smaller element than them
                # only the element smaller than current remains in the stk
                # and gets added to the res variable
                while stk and arr[stk[-1]]>=arr[i]: stk.pop()
                res[i] = n if not stk else stk[-1]
            
            # irrespective of top 3 conditions, we add curr index to stack, for future purposes.
            stk.append(i)

        return res

    def nsl(self, arr):
        n, res, stk = len(arr), [None]*len(arr), []

        for i in range(n):
            if not stk:
                res[i]=-1
            elif arr[stk[-1]]<arr[i]:
                res[i]=stk[-1]
            else:
                while stk and arr[stk[-1]]>=arr[i]: stk.pop()
                res[i] = -1 if not stk else stk[-1]
            stk.append(i)

        return res
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        To be solved using aditya verma's algorithm
        """
        if len(heights)==0: return 0
        if len(heights)==1: return heights[0]
        
        left, right = self.nsl(heights), self.nsr(heights)
        width = []
        
        # at particular index, the height we have, how wide we can use.
        # can constitute the max possible area. 
        for l, r in zip(left, right):
            width.append(r-l-1)
            
        max_area = 0
        
        for h, w in zip(heights, width):
            max_area = max(max_area, h*w)
            
        return max_area
        
        
            