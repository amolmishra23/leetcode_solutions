class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Best possible answer for this is, if area is perfect square, we can send square root.
        # if not whatever such number combination we could find, between sqrt => 1. Which is perfectly dividing the area.
        sqrt_ = int(math.sqrt(area))
        
        if sqrt_**2 == area: return [sqrt_, sqrt_]
        else:
            for i in range(sqrt_, 0, -1):
                if area%i==0:
                    return [area//i, i]
                
            