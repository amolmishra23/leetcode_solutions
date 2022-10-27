class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1_p, img2_p = [], []
        transformations = Counter()
        m, n = len(img1), len(img2)
        
        for i in range(m):
            for j in range(n):
                if img1[i][j]: img1_p.append((i,j))
                if img2[i][j]: img2_p.append((i, j))
                    
        for a,b in img1_p:
            for m, n in img2_p:
                temp = (m-a, n-b)
                transformations[temp]+=1
        
        return 0 if not transformations else max(transformations.values())