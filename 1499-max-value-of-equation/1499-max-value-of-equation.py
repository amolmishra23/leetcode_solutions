import collections

class Solution:
    """
    We have a monotonic decreasing queue, which would store the value of y-x. From greatest to smallest.
    At every index, we need to find the great possible value of (x1+y1)+(y0-x0)
    (y0-x0) we can grab it from the monotonic queue. 
    
    ** At each step we need to verify if its valid elem at front of queue. By checking if x1-x0<k or not. Else pop the element from queue beginning. 
    
    Steps to do the problem:
    1. Drop all elements which dont satisfy the criteria(**)
    2. Update res, with the best possible answer. Because its monotonic decreasing, first elem is greatest. And thus curr_x+curr_y+queue[0] should give the best possible result.
    3. Add the curr_y-curr_x in the queue. (with taking care of monotonic queue concept)
    """
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q, res = collections.deque(), float('-inf')
        
        for i, (x, y) in enumerate(points):
            # getting rid of all such points from front, whose x diff to curr point x coordinate, is greater than k.
            # because front of queue contains max element anyways, we pop it from left
            while q and abs(x - points[q[0]][0])>k: q.popleft()
            
            # finding our actual answer, with the point avlb in queue. 
            if q: res = max(res, x+y+points[q[0]][1]-points[q[0]][0])
                
            # doing the sliding window trick, to only keep monotonic decreasing queue. 
            while q and points[q[-1]][1]-points[q[-1]][0] < y-x: q.pop()
                
            # appending curr element to queue. 
            q.append(i)
            
        return res