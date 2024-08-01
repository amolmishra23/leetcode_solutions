class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(age1+age2)>60 for *phone, gender, age1, age2, seat1, seat2 in details)