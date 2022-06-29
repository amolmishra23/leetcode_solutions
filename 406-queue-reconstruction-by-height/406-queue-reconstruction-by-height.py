class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Sort based on height(descending), number of people(ascending)
        Now start inserting elements, based on how many people are permitted to be taller than it
        In the end we have our result. 
        """
        people.sort(key = lambda x: (-x[0], x[1]))
        res = deque()
        for h,k in people: res.insert(k, (h,k))
        return res