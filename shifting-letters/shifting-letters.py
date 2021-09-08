class Solution:
    def func(self, c, shift):
        return chr((ord(c)-97+shift)%26 + 97)
    
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        for i in range(len(shifts)-2, -1, -1): shifts[i] += shifts[i+1]
        return "".join(self.func(c, s) for c,s in zip(S,shifts))
        