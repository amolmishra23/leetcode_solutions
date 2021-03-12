class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        Basic logic being, we need to go on pruning the leaves which have only 1 parent. 
        An adjacency list to determine the dependencies, and then remove on the least dependent one
        In the end, we will have tree with either 1 or 2 nodes only. That is the answer. 
        """
        if n<=2: return [x for x in range(n)]
        
        neighbours = defaultdict(set)
        
        for start, end in edges:
            neighbours[start].add(end)
            neighbours[end].add(start)
            
        leaves = []
        
        for i in range(n):
            if len(neighbours[i])==1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes>2:
            remaining_nodes -= len(leaves)
            temp = []
            
            for leaf in leaves:
                for neighbour in neighbours[leaf]:
                    neighbours[neighbour].remove(leaf)
                    if len(neighbours[neighbour]) == 1:
                        temp.append(neighbour)
                        
            leaves = temp
            
        return leaves