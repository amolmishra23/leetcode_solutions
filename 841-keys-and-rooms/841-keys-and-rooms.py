class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = set()
        
        while q:
            curr_room = q.popleft()
            if curr_room in visited: continue
            visited.add(curr_room)
            
            for neigh in rooms[curr_room]:
                if neigh not in visited:
                    q.append(neigh)
                    
        return len(visited)==len(rooms)
                