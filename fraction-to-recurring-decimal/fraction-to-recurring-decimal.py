class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        res = ""
        if (n > 0 and d<0) or (n<0 and d>0): res += "-"
        
        dvd, dvs = abs(n), abs(d)
        res += str(dvd//dvs)
        
        dvd %= dvs
        if dvd: res += "."
        
        lookup = {}
        
        while dvd and dvd not in lookup:
            lookup[dvd] = len(res)
            dvd*=10
            res += str(dvd//dvs)
            dvd %= dvs
        
        if dvd in lookup: res = res[:lookup[dvd]] + "(" + res[lookup[dvd]:] + ")"
            
        return res
        