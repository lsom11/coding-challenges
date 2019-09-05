
class Codec:
    def __init__(self):
        self.urls = dict()

    def encode(self, longUrl):
        encoded = hash(longUrl)
        shortUrl = str(encoded)[:5]
        self.urls[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl):
        return self.urls[shortUrl]
