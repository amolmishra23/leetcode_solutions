class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        st = [x for x,_ in intervals]
        et = [x for _,x in intervals]
        
        st.sort(); et.sort()
        
        max_rooms, res = 0,0
        
        for start in st:
            while et and et[0]<start:
                et.pop(0)
                max_rooms-=1
            max_rooms+=1
            res = max(res, max_rooms)
            
        return res
            
        