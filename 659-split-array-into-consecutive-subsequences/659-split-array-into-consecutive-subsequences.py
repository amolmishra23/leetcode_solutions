class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Conditions given in problem
        - All subsequences should be consecutive increasing.
        - All subsequences of size 3
        
        As soon as we find subsequence less than size 3, return false
        Logic is, we count occurences of all numbers
        2 cases can happen:
        - Create a new subsequence of size 3 with this
        - Add this number to an existing subsequence of size 3 above.
        
        For case 1, we go and reduce count of num+1, num+2 and expect num+3
        For case 2, we go and reduce expect of num+3, and add another expect num+4 for future purpose.
        
        Anywhere it doesnt hit into case 1 or 2, means we have subsequence which is less than size 3. hence we can now return false. 
        """
        count, expected = Counter(nums), Counter()
        
        for num in nums:
            if count[num]==0: continue
            elif expected[num]>0:
                expected[num]-=1
                expected[num+1]+=1
            elif count[num+1]>0 and count[num+2]>0:
                count[num+1]-=1
                count[num+2]-=1
                expected[num+3]+=1
            else:
                return False
            count[num]-=1
            
        return True