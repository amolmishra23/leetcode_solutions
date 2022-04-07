class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_neigh(node):
            res = []
            for i in range(4):
                res.append(node[:i] + str((int(node[i])+1)%10) + node[i+1:])
                res.append(node[:i] + str((int(node[i])-1+10)%10) + node[i+1:])
                
            return res
        
        q = deque([("0000", 0)])
        visited = set(deadends)
        if "0000" in deadends: return -1
        
        while q:
            node, level = q.popleft()
            if node==target: return level
            for neigh in get_neigh(node):
                if neigh not in visited:
                    visited.add(neigh)
                    q.append((neigh, level+1))
                    
        return -1
        