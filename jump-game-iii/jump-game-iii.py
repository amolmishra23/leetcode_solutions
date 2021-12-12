class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """
        Simple dfs problem to explore all possible paths +/- the value of index. 
        And if we are able to reach 0, in any one of them also, then canReach is true
        Else if we return false from all of possible routes explored as false. We return false.
        
        Meanwhile we also do the bounds check, to not exceed as we do +/- of value of index. 
        And keep track of visited nodes, so that we dont get struck in a loop. 
        """
        def solve(arr, idx, visited):
            if 0<=idx<len(arr) and idx not in visited:
                if arr[idx]==0: return True
                visited.add(idx)
                return solve(arr, idx+arr[idx], visited) or solve(arr, idx-arr[idx], visited)
            return False
        
        visited = set()
        return solve(arr, start, visited)
            
            