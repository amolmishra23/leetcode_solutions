#User function Template for python3

def reverseWord(word):
    #your code here
    s,e = 0, len(word)-1
    word = list(word)
    while s<e:
        word[s], word[e] = word[e], word[s]
        s+=1
        e-=1
    return "".join(word)
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends