class Solution:
    def canPlaceFlowers(self, a: List[int], n: int) -> bool:
        """
        Check if we have a 0 slot. Then check if next slot is 0 as well, and keep adding the flowers. 
        """
        i = 0
        while i<len(a) and n:
            if a[i]==1:
                i+=2
            elif (i+1<len(a) and a[i+1]==1):
                i+=3
            else:
                n -=1
                a[i]=1
                i+=2
        
        return True if n==0 else False
    