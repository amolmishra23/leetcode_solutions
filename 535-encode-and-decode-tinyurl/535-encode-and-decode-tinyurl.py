class Codec:
    code_db, url_db = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits

    def getCode(self):
        code = "".join(random.choice(self.chars) for _ in range(6))
        return "http://tinyurl.com/"+code
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_db: return self.url_db[longUrl]
        code = self.getCode()
        while code in self.code_db: code = getCode()
        self.code_db[code] = longUrl
        self.url_db[longUrl] = code
        return code
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_db[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))