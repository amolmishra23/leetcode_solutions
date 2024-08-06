class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        key_to_num = defaultdict(list)
        
        for k,v in count.most_common():
            for i in range(2,10):
                if len(key_to_num[i])<8:
                    key_to_num[i].append(k)
                    break
                    
        res = 0
        for i in range(2, 10):
            for elem in key_to_num[i]:
                res += count[elem]*(i-1)
        
        return res