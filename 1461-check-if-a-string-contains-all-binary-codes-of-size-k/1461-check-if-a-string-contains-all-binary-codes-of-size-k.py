class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        curr, unique = deque(), set()
        
        for ch in s:
            curr.append(ch)
            if len(curr)==k:
                unique.add(tuple(curr))
                curr.popleft()
                if len(unique) == 2**k: return True
                
        return len(unique) == 2**k