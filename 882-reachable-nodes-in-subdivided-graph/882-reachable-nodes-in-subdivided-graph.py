class Solution:
    def reachableNodes(self, edges, M, N):
        # graph we draw
        e = collections.defaultdict(dict)
        # from=>to, what is the distance going to be.
        for i, j, l in edges: e[i][j] = e[j][i] = l
        
        # from node 0, we can travel for M nodes
        # reason of storing -M is, we want to use it as a minheap
        pq = [(-M, 0)]
        
        # for nodes already visited
        seen, res = set(), 0
        
        # iterate while we have not exhausted the PQ
        while pq:
            # get the current node, and number of moves possible.
            moves, i = heapq.heappop(pq)
            if i in seen: continue
            seen.add(i)
            
            # visiting the current node
            res += 1
            
            # visiting all neighbours of current node
            for j in e[i].keys():
                # if we didnt visit the neighbour
                # and also its weight+1(itself) is smaller than number of moves available.
                # we add it also in the priority queue for next time traversal
                if j not in seen and -moves>=e[i][j]+1:
                    # keeping count of remaining moves in this neighbour direction
                    # subtract total moves - all nodes count to curr node
                    # And push it to heap, that we can go remaining_moves from neighbour.
                    remaining_moves = -moves-(e[i][j]+1)
                    heapq.heappush(pq, (-remaining_moves, j))
                
                # number of moves we can make
                moves_made = min(-moves, e[i][j])
                
                # whatever moves we made we just reduce it. 
                e[i][j] -= moves_made
                e[j][i] -= moves_made
                
                # add to res as number of moves made
                res += moves_made
            
        return res