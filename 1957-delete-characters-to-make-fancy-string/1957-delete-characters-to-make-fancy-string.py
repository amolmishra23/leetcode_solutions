class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_char, prev_count = None, 0
        res = []
        for i,ch in enumerate(s):
            if ch!=prev_char:
                res.append(ch)
                prev_char, prev_count = ch, 1
            else:
                prev_count += 1
                if prev_count <= 2: res.append(ch)
                    
        return "".join(res)
                
            