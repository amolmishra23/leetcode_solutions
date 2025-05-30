class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        delta = [0]*((10**6)+2)
        
        for s,e in intervals:
            delta[s]+=1
            delta[e+1]-=1
            
        res=delta[0]
        for i in range(1, len(delta)):
            delta[i]+=delta[i-1]
            res = max(delta[i], res)
            
        return res
    
    def minGroups1(self, intervals: List[List[int]]) -> int:
        st = [x for x,_ in intervals]
        et = [x for _,x in intervals]
        
        st.sort(); et.sort()
        
        max_rooms, res = 0,0
        
        i,j = 0, 0
        while i<len(intervals):
            if st[i]<=et[j]:
                max_rooms+=1
                i+=1
            else:
                max_rooms-=1
                j+=1
            
            res = max(res, max_rooms)
            
        return res
            
        