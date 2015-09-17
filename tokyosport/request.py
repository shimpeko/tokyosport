class Request():

    BASE_URI = "https://yoyaku.sports.metro.tokyo.jp/web/"
    HOME_URI = BASE_URI + "rsvWTransUserAttestationAction.do"
    HOME_BODY = {'displayNo':"pawaa2000", 'dbInstanceNo':"1"}
    HEADERS = {'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                 , 'Accept-Charset': "UTF-8,*;q=0.5"
                 , 'Accept-Encoding': "gzip,deflate,sdch"
                 , 'Cache-Control': "max-age=0"
                 , 'Connection': "keep-alive"
                 , 'Content-Type': "application/x-www-form-urlencoded"
                 , 'Host': "yoyaku.sports.metro.tokyo.jp"
                 , 'Origin': "https://yoyaku.sports.metro.tokyo.jp"
                 , 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.45 Safari/537.17"}

    def __init__(self, action, body, headers=None):
        self.__uri = Request.BASE_URI + action
        self.__body = self.__make_body(body)
        if headers != None:
            self.__headers = dict(self.__default_headers).update(headers)
        else:
            self.__headers = self.HEADERS

    @property
    def uri(self):
        return self.__uri 
    
    @property
    def body(self):
        return self.__body

    @property
    def headers(self):
        return self.__headers

    def __make_body(self, body):
        if isinstance(body, dict):
            return self.to_http_param(body)
        else:
            return body

    @staticmethod
    def to_http_param(body):
        return "&".join(k+"="+str(v) for k, v in body.items())

if __name__ == '__main__':
    r = Request("action", {"a":1,"b":2})
    print(r.uri)
    print(r.body)
