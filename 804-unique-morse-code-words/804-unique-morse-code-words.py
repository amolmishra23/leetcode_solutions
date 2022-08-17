class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        eng = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set(["".join([eng[ord(ch)-97] for ch in word]) for word in words]))