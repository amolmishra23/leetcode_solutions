class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        Whole idea is that, instead of coming from ??? to abc, come from abc to ???
        by replacing whatever occurences of stamp that we find
        in the end we just return when we cant make any further operations. or we have fully transitioned to target
        """
        def okay(s):
            res = False
            for a, b in zip(s, stamp):
                if a=="?": continue
                elif a!=b: return False
                else: res = True
            return res
        
        end, move, res = "?"*len(target), 0, []
        
        while True:
            pre = move
            for i in range(len(target)-len(stamp)+1):
                if okay(target[i:i+len(stamp)]):
                    move += 1
                    res.append(i)
                    target = target[:i]+"?"*len(stamp)+target[i+len(stamp):]
            if target == end: return res[::-1]
            if move == pre: break
        return []