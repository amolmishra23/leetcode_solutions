class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = int(10 ** 9 + 7)

        freq_dict = dict()

        for point in points:

            if(point[1] not in freq_dict):
                freq_dict[point[1]] = 1
            else:
                freq_dict[point[1]] += 1
        
        for y, freq in freq_dict.items():
            freq_dict[y] = comb(freq, 2)
        
        ans = 0
        ps = 0

        for e in freq_dict.values():
            ans = (ans + e * ps) % mod 
            ps = (ps + e) % mod 
        
        return ans 