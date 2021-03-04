class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        
        for i, s in enumerate(sandwiches):
            if not count[s]:
                break
            count[s]-=1
        else:
            i = len(sandwiches)

        return len(sandwiches)-i