class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: return False

        rev_num = 0
        x_copy = x
        
        while x:
            rev_num = (rev_num*10) + x%10
            x /= 10
            
        return x_copy == rev_num