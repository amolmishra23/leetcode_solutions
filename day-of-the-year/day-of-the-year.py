class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int, date.split("-"))
        return int((datetime.datetime(y,m,d) - datetime.datetime(y,1,1)).days + 1)