class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Catch is that for the count we store digit wise in the array as strings
        We solve this using simple 2 pointer approach, to keep moving until we find the same letter.
        Once we are done finding same letter, we add it to the same array
        This problem is done in O(1) space complexity
        """
        ans, i = 0, 0
        
        while i<len(chars):
            letter = chars[i]
            count = 0
            
            while i<len(chars) and chars[i]==letter:
                count += 1
                i += 1
            
            chars[ans] = letter
            ans += 1
            
            if count>1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
                    
        return ans