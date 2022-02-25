class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Split string at every k, and check
        1. left is palindrome, and reverse of right exists in string
        2. right is palindrome, and reverse of left exists in string
            
        Return the output. 
        """
        
        wordict = {}
        res = [] 
        for i in range(len(words)):
            wordict[words[i]] = i
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                # we start from j=0 so that in 1st attempt we will have tmp1="" and tmp2=words[i]
                # now we will also the cover case to check if words[i][::-1] exists in the string or not. 
                
                tmp1 = words[i][:j]
                tmp2 = words[i][j:]
                
                # reverse of tmp1 exists
                # tmp2 is actually a palindrome
                
                if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                    res.append([i,wordict[tmp1[::-1]]])
                # reverse of tmp2 exists
                # tmp1 is actually a palindrome. 
                
                if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
                    res.append([wordict[tmp2[::-1]],i])

        return res