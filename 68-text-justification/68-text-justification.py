class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, i = [], -1
        
        while i<len(words)-1:
            # ws means with space
            # wos means without space
            len_wos, len_ws, curr = 0, 0, []
            
            while i<len(words)-1:
                # if we are exceeding max width, we can break
                if len_ws+len(words[i+1]) > maxWidth: break
                # add word to the curr list
                curr.append(words[i+1])
                # adding the length with space, without space. 
                len_ws += len(words[i+1])+1
                len_wos += len(words[i+1])
                i+=1
            
            # finding total spaces needed to be inserted.
            # equal to number of chars in the row minus the total length of field
            spaces_needed, temp = maxWidth-len_wos, []
            
            # if we have atleast 2 word
            if len(curr)>1:
                # if we are at last word
                if i==len(words)-1:
                    # in last row, no need to justify stuff
                    # so for normal words, add with 1 space
                    # after last word in the last line, we will add number of final spaces to make the line justified
                    for j, word in enumerate(curr):
                        temp.append(word)
                        temp.append(" "*(maxWidth-len(''.join(temp))) if j==len(curr)-1 else " ")
                # if not at the last word
                else:
                    # find number of spaces between each word
                    # and number of extra spaces(remainder)
                    quo, rem = divmod(spaces_needed, len(curr)-1)
                    for j, word in enumerate(curr):
                        # add the word to the temp
                        temp.append(word)
                        # if at last word no need to add extra spaces
                        if j==len(curr)-1: break
                        # add the required spaces
                        temp.append(" "*quo)
                        # if any extra spaces, add that as well
                        if rem: temp.append(" "); rem-=1
            else:
                # add the only 1 word, and number of spaces required
                temp.append(curr[0])
                temp.append(" "*spaces_needed)
            
            # adding the curr line into final result variable
            res.append("".join(temp))
            
        return res