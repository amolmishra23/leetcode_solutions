class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, i = [], -1
        
        while i<len(words)-1:
            len_wos, len_ws, curr = 0, 0, []
            
            while i<len(words)-1:
                if len_ws+len(words[i+1]) > maxWidth: break
                curr.append(words[i+1])
                len_ws += len(words[i+1])+1
                len_wos += len(words[i+1])
                i+=1
            
            spaces_needed, temp = maxWidth-len_wos, []
            
            if len(curr)>1:
                if i==len(words)-1:
                    for j, word in enumerate(curr):
                        temp.append(word)
                        temp.append(" "*(maxWidth-len(''.join(temp))) if j==len(curr)-1 else " ")
                else:
                    quo, rem = divmod(spaces_needed, len(curr)-1)
                    for j, word in enumerate(curr):
                        temp.append(word)
                        if j==len(curr)-1: break
                        temp.append(" "*quo)
                        if rem: temp.append(" "); rem-=1
            else:
                temp.append(curr[0])
                temp.append(" "*spaces_needed)
            
            res.append("".join(temp))
            
        return res