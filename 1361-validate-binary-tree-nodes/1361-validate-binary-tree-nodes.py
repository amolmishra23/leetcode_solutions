class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree=[0]*(n)
        
        for l,r in zip(leftChild, rightChild):
            if l!=-1: indegree[l]+=1
            if r!=-1: indegree[r]+=1
            if indegree[l]>1 or indegree[r]>1: return False
            
        sources = deque(i for i,d in enumerate(indegree) if d==0)
        if len(sources)>1: return False
                
        res = []
        while sources:
            curr = sources.popleft()
            res.append(curr)
            
            for child in leftChild[curr], rightChild[curr]:
                indegree[child]-=1
                if indegree[child]==0: 
                    sources.append(child)
            
        return len(res)==n
        