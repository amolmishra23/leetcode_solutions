class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set()
        
        while q:
            curr_node = q.popleft()
            if curr_node in visited: continue
            
            visited.add(curr_node)
            
            for neigh in rooms[curr_node]:
                if neigh not in visited: q.append(neigh)
                    
        return len(visited)==len(rooms)