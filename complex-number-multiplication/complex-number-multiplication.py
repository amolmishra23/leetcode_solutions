class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(s):
            real, img = s.split("+")
            real = int(real)
            img = int(img[:-1])
            
            return (real, img)
        """
        (a+bi)(c+di)
        ac+adi+bci-bd
        (ac-bd)+i(ad+bc)
        """
        
        a, b = parse(num1)
        c, d = parse(num2)
        x = a*c - b*d
        y = a*d + b*c
        
        return str(x)+"+"+str(y)+"i"
        
        
        