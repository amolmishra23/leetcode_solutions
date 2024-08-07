class Solution:
    def numberToWords(self, num: int) -> str:
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["Thousand","Million","Billion"]
        
        def to_words(num):
            if num==0: return []
            elif num<20: return [self.lessThan20[num]]
            elif num<100: return [self.tens[num//10]]+to_words(num%10)
            elif num<1000:
                q, r = num//100, num%100
                return [self.lessThan20[q], 'Hundred'] + to_words(r)
            
            for power, thousand in enumerate(self.thousands, 1):
                # the least number would be 100 thousand.
                # we check its below which number. 
                if num < 1000 ** (power+1):
                    temp = 1000**power
                    q, r = num//temp, num%temp
                    return to_words(q) + [thousand] + to_words(r)
                
        return ' '.join(to_words(num)).strip() or 'Zero'
            