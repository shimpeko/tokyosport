from session import Session
from request import Request
from request_body import RequestBody
import datetime
import re

class Client:

    __PLAY_ACTION = "rsvWTransInstSrchPpsAction.do"
    __PARK_ACTION = "rsvWTransInstSrchMultipleAction.do"
    __SLOT_ACTION = "rsvWGetInstSrchInfAction.do"
    __BACK_ACTION = "rsvWInstSrchVacantBackAction.do"

    def __init__(self):
        self.__session = None
        self.__last_requested_sport = None


    def __get_valid_session(self, sport=None):
        if self.__has_valid_session() is True \
           and (self.__last_requested_sport == sport \
                or self.__last_requested_sport is None):
            return self.__session
        self.request_sports()
        self.__last_requested_sport = sport
        return self.__session
    
    def __has_valid_session(self):
        if self.__session is None:
            return False
        if (datetime.datetime.today() - self.__session.last_use).seconds > 60:
            return False
        return True

    def request_sports(self):
        self.__session = Session()
        self.request_months(self.__session)
        request_body = RequestBody().content
        return self.__session.request(Request(self.__PLAY_ACTION, request_body))

    def request_parks(self, sport):
        rb = RequestBody(sport).content
        return self.__get_valid_session(sport).request(
               Request(self.__PARK_ACTION, rb))

    def request_slots(self, sport, yearmonth, days, park):
        request_body = RequestBody(sport, yearmonth, days, park).content
        response, content = self.__get_valid_session(sport).request(
                            Request(self.__SLOT_ACTION, request_body))
        self.__request_back()
        return response, content

	
    
    def request(self, play=None, yearmonth=None, days=None, park=None):
        if yearmonth == None:
            yearmonth = self.current_yearmonth()
        session = Session()
        self.request_months(session)
        request_body = RequestBody().content
        response, content = session.request(Request(self.__PLAY_ACTION
                                                    , request_body))
        if play == None:
            return response, content
        request_body = RequestBody(play).content
        response, content = session.request(Request(self.__PARK_ACTION
                                                    , request_body))
        if park == None or yearmonth == None or days == None:
            return response, content
        self.__session = session
        self.__last_requested_play = play
        return self.request_slots(play, yearmonth, days, park)
                                                  
    def __request_back(self):
        self.__session.request(Request(self.__BACK_ACTION
                                       , {'displayNo': "prwca1000"}))
    @staticmethod
    def request_months(session=None):
        if session == None:
            session = Session()
        response, content  = session.request(Request(session.action
                                                 , {'displayNo': "prwaa1000"}))
        po = re.compile("changeMonthGif")
        lines = []
        for line in content.decode('shift_jis').splitlines():
            if po.search(line) != None:
                lines.append(line)
        months = []
        for month in range(1,12):
            for line in lines:
                if re.search(str(month)+"月", line) != None:
                    months.append(month)
        return months

    @staticmethod
    def current_yearmonth():
        today = datetime.date.today()
        ten_days = datetime.timedelta(days=10)
        if today.day >= 22:
            return (today + ten_days)
        else:
            return today
