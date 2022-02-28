from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """
        In order to find the largest overlap, we find all the indexes where 1 is present in both source and target images
        Next we find the distances of each source 1 pixel to target pixel. 
        Maximum number of matches we get, is the result. 
        """
        n = len(img1)
        img1_ones = []
        img2_ones = []
        
        
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    img1_ones.append((i, j))
                if img2[i][j]==1:
                    img2_ones.append((i, j))
                
        movement = defaultdict(int)
        max_val = 0
        print (img1_ones, img2_ones);
        for i, j in img1_ones:
            for m, n in img2_ones:
                #(m-i, n-j) actually denotes a probable rotation
                # with the same rotation, if multiple pixels rotate, we can get multiple overlaps
                # return the maximum overlaps in the end
                movement[
                    (m-i, n-j)
                ] += 1
                max_val = max(max_val, movement[(m-i, n-j)])
        
        return max_val