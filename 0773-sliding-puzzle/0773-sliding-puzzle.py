class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neigh = {
            0: [1,3],
            1: [0, 4, 2],
            2: [1, 5],
            3: [0, 4],
            4: [1,3,5],
            5: [2,4],
        }
        start = "".join([str(elem) for row in board for elem in row])
        queue = deque(); queue.append((start, 0))
        visited = set(); visited.add(start)
        
        while queue:
            state, moves = queue.popleft()
            
            if state == "123450":
                return moves
            
            zero_index = state.index("0")
            
            for n in neigh[zero_index]:
                new_state = list(state)
                new_state[zero_index], new_state[n] = new_state[n], new_state[zero_index]
                new_state_str = "".join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves+1))
                    
        return -1
        