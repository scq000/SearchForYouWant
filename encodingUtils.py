import urllib2
from gzip import GzipFile
from StringIO import StringIO
import zlib

class EncodingUtils:
    def __init__(self):
        self.url = ''
        self.encoding = 'utf8'
        self.content = ''

    def start(self,url):
        self.url = url
        self.set_encoding()
        self.get_data()
        return self.content

    def get_data(self):
        self.set_encoding()
        if self.encoding == 'gzip':
            self.gzip()
        elif self.encoding == 'deflate':
            self.deflate()

    def set_encoding(self):
        request = urllib2.Request(self.url)
        request.add_header('Accept-encoding', 'gzip,deflate')
        response = urllib2.urlopen(request)
        self.content = response.read()
        self.encoding = response.info().get('Content-Encoding')

    def gzip(self):
        buf = StringIO(self.content)
        f = GzipFile(fileobj=buf)
        self.content = f.read()

    def deflate(self):
        try:
            self.content = zlib.decompress(self.content, -zlib.MAX_WBITS)
        except zlib.error:
            self.content = zlib.decompress(self.content)