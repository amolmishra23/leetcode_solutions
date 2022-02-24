class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = sum(a==b for a,b in zip(secret, guess))
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return "%dA%dB" % (bull, both-bull)