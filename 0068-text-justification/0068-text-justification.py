class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr_list, curr_length = [], 0
        res = []
        
        for word in words:
            if len(curr_list)+curr_length+len(word)>maxWidth:
                num_spaces = maxWidth-curr_length
                if len(curr_list)==1:
                    res.append(curr_list[0] + ' '*(num_spaces))
                else:
                    std_spaces, extra_spaces = divmod(num_spaces, len(curr_list)-1)
                    for i in range(extra_spaces):
                        curr_list[i]+=" "
                    temp = (" "*std_spaces).join(curr_list)
                    res.append(temp)
                curr_list, curr_length = [], 0
            curr_list.append(word)
            curr_length += len(word)
        
        if curr_list and curr_length:
            num_spaces = maxWidth-curr_length
            temp = " ".join(curr_list)
            temp += " "*(num_spaces-(len(curr_list)-1))
            res.append(temp)
            
        return res