class Solution:
    def func(self, c, shift):
        return chr((ord(c)-97+shift)%26 + 97)
    
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        # as per question, we shift first i+1 letters.
        # means when shifting 0, we need to shift from 0 to i+1
        # when shifting i, we only need to shift from i to i+1
        # hence like prefix 
        for i in range(len(shifts)-2, -1, -1): 
            shifts[i] += shifts[i+1]
        
        # finally make the number of shifts, and make the final string. 
        return "".join(self.func(c, s) for c,s in zip(S,shifts))
        