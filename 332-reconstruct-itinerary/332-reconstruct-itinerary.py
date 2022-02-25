import collections
import heapq

class Solution:
    def solve(self, node):       
        # performing a topological sort in dfs fashion
        # to traverse the nodes in proper order.
        while self.graph[node]:
            temp = heapq.heappop(self.graph[node])
            self.solve(temp)
            
        self.res.append(node)
            
        
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        We combine 3 data structures to solve this problem. 
        Graph
        Adjacency list, where list is sorted. (for lexicographical order) 
        Stack. 
        
        We keep pushing elements to stack in dfs fashion, until we have elements in adjacency list
        Once we visit such a element, whose adjacency list is empty, we pop it from stack and push it to result
        finally we reverse the array and return the result. 
        
        """
        self.graph = collections.defaultdict(list)
        n = len(tickets)
        
        for src, dst in tickets:
            heapq.heappush(self.graph[src], dst)
        
        self.res = []
        self.solve("JFK")
    
        return reversed(self.res)