import httplib2
import re
from request import Request
import datetime

class Session:
    def __init__(self):
        # construct httplib2
        # httplib2.debuglevel=100
        self.__h = httplib2.Http(disable_ssl_certificate_validation=True)
        self.__p_sid = re.compile("(JSESSIONID=.*?);")
        self.__sid = ""
        self.__action = "" 
        self.__last_use = None

    def __request_action(self):
        action= "rsvWTransInstSrchVacantAction.do"
        body = {'displayNo': "pawae1000"}
        response, content = self.request(Request(action, body))
        ps = "^\s*var\sgRsvWTransInstSrchMultipleAction.*'/web/(.*\.do)';$"
        po = re.compile(ps)
        for line in content.decode('shift_jis').splitlines():
            r = po.match(line)
            if r != None:
                return r.group(1)

    def __request_sid(self, uri, method="POST", headers=None
                      , cookie=None, body=None):
        if headers == None:
            headers = Request.HEADERS
        if cookie != None:
            headers = dict(headers, Cookie=cookie)
        response, content = self.__h.request(uri, method, headers=headers
                                             , body=body)
        return self.__p_sid.match(response['set-cookie']).group(1)

    @property
    def sid(self):
        if self.__sid != "":
            return self.__sid
        base_sid = self.__request_sid(Request.BASE_URI, method="GET")
        self.__sid = self.__request_sid(Request.HOME_URI, cookie=base_sid
                     , body=Request.to_http_param(Request.HOME_BODY))
        return self.__sid

    @property
    def action(self):
        if self.__action != "":
            return self.__action
        self.__action = self.__request_action()
        return self.__action

    @property
    def last_use(self):
        return self.__last_use

    def request(self, request):
        h = dict(request.headers)
        h['Cookie'] = self.sid
        h['Content-Length'] = str(len(request.body))
        self.__last_use = datetime.datetime.today()
        return self.__h.request(request.uri, "POST",  headers=h, body=request.body)
if __name__ == '__main__':
    s = Session()
    print(s.sid)
    print(s.last_use)
        
