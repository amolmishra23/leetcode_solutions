class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count, unique_idx = Counter(arr), 0
        for char in arr:
            if count[char]==1:
                unique_idx += 1 
                if unique_idx == k: return char
            
        return ""