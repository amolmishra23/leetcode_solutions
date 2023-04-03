# class Solution:
#     def numRescueBoats(self, people: List[int], limit: int) -> int:
#         people.sort()
#         def possible(boats):
#             l, h = 0, len(people)-1
            
#             while l<=h:
#                 if people[l]+people[h]<=limit:
#                     l+=1; h-=1; boats-=1
#                 else:
#                     h-=1; boats-=1
#                 if boats<0: return False
                
#             return boats>=0
            
#         l, r = 1, len(people)
        
#         while l<r:
#             m = l + (r-l)//2
#             if possible(m):
#                 r = m
#             else:
#                 l = m+1
        
#         return l

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        lo = 0
        hi = len(people)-1
        boats = 0
        while lo <= hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            boats += 1
        return boats