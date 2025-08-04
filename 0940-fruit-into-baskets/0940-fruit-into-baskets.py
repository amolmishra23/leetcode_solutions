class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = Counter()
        i, res = 0, float("-inf")

        for j in range(len(fruits)):
            curr_fruit = fruits[j]
            count[curr_fruit]+=1

            while len(count)>2:
                start_fruit=fruits[i]
                count[start_fruit]-=1
                if count[start_fruit]==0: del count[start_fruit]
                i+=1

            res = max(res, j-i+1)

        return res