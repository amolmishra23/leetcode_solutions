class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def next_greater(arr):
            res = [None]*len(arr)
            stk = []
            
            # typical AV solution to find the next greater element
            for i in range(len(arr)-1, -1, -1):
                # pop out all the elements, until we dont have a greater element than curr element
                # we pop even the equal element, as this element would hold a precedence for the next greater element. 
                while stk and arr[stk[-1]]<=arr[i]: stk.pop()
                
                # result is the next greater element after this number
                if stk:
                    res[i] = stk[-1]
                else:
                    res[i] = 0
                
                # we append this element, as it could be a potential solution for numbers on the left
                stk.append(i)
            
            # this hardwork we do because, we need not next greater index, but no of days, from current day
            for i in range(len(res)):
                res[i] = max(res[i]-i, 0)
            
            return res
        
        return next_greater(temperatures)
            