class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        """
        Rabbit says the count of how many others like it. 
        It doesn't really say which colour it is. 
        We need to group into imaginary groups based on the count mentioned. 

        [1,1,1] => 1,1 can be grouped in same color. their saying 1 is basically (1+1)
        but 3rd 1 needs to be on separate group and needs to have a partner
        total count is 4.

        this can be computed as math.ceil(count[1]/2) * 2
        """
        count = Counter(answers)
        res = 0

        for x in count:
            group_size = x+1
            number_of_groups = math.ceil(count[x] / group_size)
            res += (group_size * number_of_groups)

        return res