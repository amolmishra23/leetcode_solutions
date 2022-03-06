from collections import deque

class Solution:
    """
    Same monotonic queue concept to solve the problem.
    
    Here slight change. 
    1. We add the new element -> satisfying monotonic property
    2. We remove the elements which dont satisfy criteria
    3. And we update the result. 
    
    To solve this problem, we need to store all the maximum and minimum values in a sliding window approach
    What is the biggest element starting at index 2? The answer to this can be given by...
    For same, we use a deque, (max and min)
    
    While inserting in max_dq, element before me, must be bigger than me. elements are decreasing (10,5,4,3). 
    Before inserting 5, clear all the elements less than 5.
    While inserting in min_dq, elements before me, must be smaller than me. elements are increasing (3,5,10)
    
    We have a left and right pointer. Between left and right pointer, the min and max elements we have in deque respectively. 
    (because the queue are monotonic, we are sure to have max and min elements at begin of queue respectively)
    
    For a particular range we keep checking, if max-min<limit. Then we update the result with right-left+1
    If for suppose the condition isnt satisified, we move the left pointer by 1. In case our left pointer was the max or min element, we pop it off from our monotonic queue respectively
    """
    def longestSubarray(self, A, limit):

        # This is a monotonically decreasing double-ended queue. 
        maxd = collections.deque()

        # This is a monotonically increasing double-ended queue.
        mind = collections.deque()

        i = 0
        for j in range(len(A)):
            # At each iteration, we maintain the biggest elements in maxd.
            # Remove any element smaller than A[j]
            while len(maxd) and A[j] > maxd[-1]: maxd.pop()

            # At each iteration, we maintain the smallest elements in mind.
            # Remove any element bigger than A[j]
            while len(mind) and A[j] < mind[-1]: mind.pop()

            # Why do we always add A[j] ?
            # As we will see below, we may have to remove an element(may be A[j-1] if i was j-1) 
            # from the beginning of the maxd/mind.
            # After that, we still need to know the max/min numbers from A[i/i+1]...A[j]
            maxd.append(A[j])
            mind.append(A[j])

            # maxd holds the biggest elements from A[i]...A[j] in decreasing order.
            # So maxd[0] is the biggest element in the window A[i]...A[j]
            # mind holds the smallest elements from A[i]...A[j] in increasing order.
            # So mind[0] is the smallest element in the window A[i]...A[j]
            # maxd[0]-mind[0] is the biggest difference in the window A[i]...A[j]
            if maxd[0] - mind[0] > limit:
                # The biggest difference is over the limit; so remove A[i] from the window.
                # Why do we check only maxd[0]/mind[0] to remove A[i]?
                # Take maxd as an example. In order for A[i] to be present in maxd, 
                # A[i] >= A[x], where x = i+1...j. In other words, it has to be the biggest element or 
                # it would have already been removed. The biggest element would be in maxd[0]. 
                # Similar explanation applies for mind.
                if maxd[0] == A[i]: maxd.popleft()
                if mind[0] == A[i]: mind.popleft()
                # The new window for consideration is A[i+1]...A[j].
                i += 1

        # At every iteration of j, the window size for consideration is from A[i..j]. Its size is j+1-i.
        # At every iteration, an element is added to the window and possibly removed only if the window contains
        # elements with max difference > limit.
        # So the window size only grows monotonically but never shrinks in size. The window grows only if all the elements in
        # the window satisfy the max difference <= limit.
        # Therefore, the last window size in the iteration(when j=len(A)-1) holds the maximum size of the window with max diff <= limit.
        # However, it must be noted that the window in consideration at the last iteration may not really be the window
        # which has the max diff <= limit.
        # This doesn't matter since all we are interested in is the window size and not really the elements in the window.
        return len(A) - i