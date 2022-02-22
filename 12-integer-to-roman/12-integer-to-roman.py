class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        number_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10:"X",\
            40: "XL", 50: "L", 90: "XC", 100: "C",\
            400: "CD", 500: "D", 900: "CM", 1000: "M"
        }
        
        keyset, result = sorted(number_map.keys(), reverse=True), []
        
        while num>0:
            """
            The trick is, because upper limit is only 4000.
            We keep dividing by 1000 to check, which num range does it fall into.
            We keep subtracting that
            Finally add the correct roman to the string result.
            """
            for key in keyset:
                while num/key>0:
                    num-=key
                    result += number_map[key]
                    
        return "".join(result)