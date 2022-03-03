from string import ascii_lowercase, ascii_uppercase

class Solution:
    def toLowerCase(self, str: str) -> str:
        keys, values = list(ascii_lowercase)+list(ascii_uppercase), list(ascii_lowercase)*2
        mapping = dict(zip(keys, values))
        
        return ''.join(map(lambda x: mapping.get(x, x), list(str)))
        