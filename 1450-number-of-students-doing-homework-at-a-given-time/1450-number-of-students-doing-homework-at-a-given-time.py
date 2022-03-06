class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(
            start_time<=queryTime<=end_time for start_time, end_time in zip(startTime, endTime)
        )