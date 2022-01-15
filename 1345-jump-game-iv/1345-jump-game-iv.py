class Solution:
    def minJumps(self, arr: List[int]) -> int:
        map_, n = defaultdict(list), len(arr)
        
        # if only 1 element, we are already at destination
        if n==1: return 0
        
        # caching for the indexes of all elements. will help us while doing bfs
        for i,x in enumerate(arr):
            map_[x].append(i)
            
        # queue and number of steps we have made
        q, step = deque([0]), 0
        
        while q:
            # we currently made 1 step
            step += 1
            
            for _ in range(len(q)):
                #popping the 1st element.
                x = q.popleft()
                
                # we can add num-1, num+1 indexes
                if x-1>=0 and arr[x-1] in map_:
                    q.append(x-1)
                
                if x+1<=n-1 and arr[x+1] in map_:
                    if x+1==n-1: return step
                    q.append(x+1)
                
                # adding other indexes of the same number to queue
                if arr[x] in map_:
                    for y in map_[arr[x]]:
                        if y!=x: 
                            if y==n-1: return step
                            q.append(y)
                    
                # in order to mark number as actually visited, we remove it from queue. 
                # so next time it wont again go in a continuous loop. 
                # its other indexes are anyways taken care through adding in queue, 1st time itself. 
                if arr[x] in map_: del map_[arr[x]]
                            
        return step
                