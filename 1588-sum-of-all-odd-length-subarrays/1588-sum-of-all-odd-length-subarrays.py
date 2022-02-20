class Solution:
    def sumOddLengthSubarrays(self, A: List[int]) -> int:
        """
        For One pass solution we need to know how many times each number was part of a subarray.
        Here we have constarints that

        at each digit, it should be part of subarray.
        It can add values on both left and right to form a subarray.
        lets take a example arr: [5,6,7,3,4,5,6,2]

        Here lets take 4 to find out how many subarrays its a part of then we can move to odd sized subarrays.

        4 at a index 4(lets call it 'idx') and size of array is 8.
        To the left of 4 there are idx count of numbers, for them to be part of subarray including 4 you can either choose zero or one or two or three or four of them. i.e it can be [4], [3,4], [7,3,4], [6,7,3,4], [5,6,7,3,4] so you can do this in 5 ways which is (idx+1).
        Now for each of this (idx+1) subarrays you can add values of the right.
        On right we have (n-idx-1) numbers, so we can choose either zero or one or .... or n-idx-1 numbers and add them to anyof our already subarrays. we have n-idx choices and they can be added to any of idx+1 choices. total become (idx+1)*(n-idx) subarrays.
        Note: think of it this way you have m blue tickets and n red tickets you choose them in (m+1)*(n+1) ways

        Now totals subarrays which contains number at idx became (idx+1)*(n-idx) , Now we need to see how many of them are ODD sized.

        if total count is even we can say both even and odd are equal and divide by 2 will suffice.

        if total count is odd thats mean idx+1 is odd and n-idx is odd. There is a big explanation why odd will be more in that case. By intuition you can say odd will be more. I will update If I get a simpler explanation on why odd will be more.

        so odd sized will be ((idx+1)(n-idx)+1)/2 or you can divide and use ceil on it.


        """
        res, n = 0, len(A)
        for i, a in enumerate(A):
            res += ((i + 1) * (n - i) + 1) // 2 * a
        return res