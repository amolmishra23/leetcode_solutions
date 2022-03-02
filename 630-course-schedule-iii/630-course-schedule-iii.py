class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        very tricky question.
        We sort the courses by their expected deadline.
        Now one by one we start doing the courses.
        If by chance, we are exceeding the deadline. We tend to eliminate the courses, which take max time so as to accomodate more number of min time courses. If we have 6 minutes, better to do 4+2(2 courses) instead of 1 course(5)
        """  
        if courses == None or len(courses) == 0:
            return 0
        
        courses.sort(key = lambda x: (x[1], x[0]))
        curr_time = count = 0
        max_heap = []
        heapify(max_heap)
		
        for i in range(len(courses)):
            """
            Goal here is to do maximum number of courses.
            For this, we need to pick up courses with minimal number of days requirement also. (We use min-heap for this)
            In addition to picking courses on their deadline. (We sort the array based on this)
            
            [[5,5],[4,6],[2,6]]
            This example helps to decide why we need heap here. 

            1. heap = [[5,5]]
            2. heap = [[4,6]]. Now it is actually exceeding the time limits. 
            So we will pop out the course which takes max time. (5) here. 
            """
            heappush(max_heap, -1 * courses[i][0])
            curr_time += courses[i][0]
            count += 1
			
            if  curr_time > courses[i][1] :
                curr_time += heappop(max_heap)
                count -= 1

        return count
        