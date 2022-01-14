class Solution:
    def myAtoi(self, s: str) -> int:
        # clear all the extra spaces
        s = s.strip()
        digits_map = {str(k):k for k in range(10)}
        signs = {"+", "-"}
        space = " "
        curr_sign, res = None, None
        
        for char in s:
            if char in signs:
                if curr_sign is None and res is None:
                    # only one sign char is allowed. if we get that, we cache it
                    curr_sign = char
                else:
                    # if we got sign char for 2nd time, we just return whatever result we computed
                    if res is None: return 0
                    return -res if curr_sign=="-" else res
            elif char in digits_map:
                if res is None: res = 0
                res *= 10
                # store the char in res variable whatever came
                res += digits_map[char]
            else:
                # as soon as we find the first wrong char, return
                break
        
        if res is not None and curr_sign == "-": res = -res
        
        # limiting it to min and max. 
        if res is None: return 0
        elif res>0:
            return min(res, 2**31-1)
        else:
            return max(res, -2**31)
                