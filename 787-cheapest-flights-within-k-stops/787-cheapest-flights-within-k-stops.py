class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        A good case to practice Dijkstra.

        To implement Dijkstra, we need a priority queue to pop out the lowest weight node for next search. In this case, the weight would be the accumulated flight cost. So my node takes a form of (cost, src, k). cost is the accumulated cost, src is the current node's location, k is stop times we left as we only have at most K stops. I also convert edges to an adjacent list based graph g.

        Use a vis array to maintain visited nodes to avoid loop. vis[x] record the remaining steps to reach x with the lowest cost. If vis[x] >= k, then no need to visit that case (start from x with k steps left) as a better solution has been visited before (more remaining step and lower cost as heappopped beforehand). And we should initialize vis[x] to 0 to ensure visit always stop at a negative k.

        Once k is used up (k == 0) or vis[x] >= k, we no longer push that node x to our queue. Once a popped cost is our destination, we get our lowest valid cost.

        For Dijkstra, there is not need to maintain a best cost for each node since it's kind of greedy search. It always chooses the lowest cost node for next search. So the previous searched node always has a lower cost and has no chance to be updated. The first time we pop our destination from our queue, we have found the lowest cost to our destination.
        """
        f = defaultdict(dict)
        
        for a,b,p in flights:
            f[a][b] = p
            
        heap = [(0, src, k+1)]
        vis = [0]*n
        
        while heap:
            # [cost, node, k_remaining]
            p,i,k = heapq.heappop(heap)
            # if we reached destination, return the cost
            if i==dst: return p
            
            # to avoid cycles and not to visit it again
            if vis[i]>=k: continue
            vis[i]=k
            
            if k>0:
                for j in f[i]:
                    heapq.heappush(heap, (p+f[i][j], j, k-1))
                    
        return -1