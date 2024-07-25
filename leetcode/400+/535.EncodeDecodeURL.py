import string, random
class Codec:

    def __init__(self) -> None:
        self.map = {}
        self.pool = string.ascii_lowercase + string.digits
        self.random_chars = random.choices(self.pool, k=5)
        self.random_string = ''.join(self.random_chars)

    def encode(self, longUrl: str) -> str:
        shortURL = self.random_string
        self.map[shortURL] = longUrl
        
        return 'http//tinyurl/' + shortURL        

    def decode(self, shortUrl: str) -> str:
        shortUrl = shortUrl.split('/')[-1]
        longURL = self.map[shortUrl]
        return longURL
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))