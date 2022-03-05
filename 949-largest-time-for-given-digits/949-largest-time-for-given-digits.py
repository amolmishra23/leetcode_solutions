class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        """
        [1,2,3,4] => combinations are 1,2,3--2,3,4--1,3,4
        Permutations are 1,2,3--2-1-3.....
        So generate all permutations of sorted numbers. And see whichever is the 1st valid time, we return it to the client. 
        """
        result = ""
        
        arr.sort(reverse=True)
        
        for h1, h2, m1, m2 in itertools.permutations(arr):
            hours = 10*h1+h2
            mins = 10*m1+m2
            
            if 0<=hours<24 and 0<=mins<60:
                result = "{:02}:{:02}".format(hours, mins)
                break
        
        return result