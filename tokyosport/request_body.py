import datetime
import copy
from collections import OrderedDict

class RequestBody:

    __DEFAULT_SEARCH_PARAMS = OrderedDict([('displayNo', 0)
                       , ('selectAreaCd', 0)
                       , ('selectBldCd', 0)
                       , ('selectPpsdCd', 0)
                       , ('selectPpsCd', 0)
                       , ('selectPpsPpsdCd', 0)
                       , ('selectInstNo', 0)
                       , ('dispWeekNum', 0)
                       , ('dispWeek', [0] * 8)
                       , ('submmitMode', 1)
                       , ('conditionMode', 3)
                       , ('transVacantMode', 8)
                       , ('dispSelectInstBldCd', 0)
                       , ('dispSelectInstCd', 0)
                       , ('selectCommunityManageCd', 0)
                       , ('selectCommunityPlaceCd', 0)
                       , ('productMode', 3)
                       , ('areaMode', 2)
                       , ('dispMonth', 0)
                       , ('stateMonth', 1)
                       , ('dispYMD', 0)
                       , ('selectM', 0)
                       , ('selectYMD', 0)
                       , ('e430000', "%97%98%97p%8C%8E%82%F0%91I%91%F0%82%B5%82"
                                     "%C4%82%AD%82%BE%82%B3%82%A2%81B")
                       , ('bldBtnStat', [0] * 27)
                       , ('selectBldCdsNum', 0)
                       , ('e510060', "%8C%F6%89%80%82%F0%91I%91%F0%82%B5%82%C4%"
                                     "82%AD%82%BE%82%B3%82%A2%81B")])

    def __init__(self
                 , sport=None
                 , yearmonth=None
                 , days=None
                 , parks=None):
        self.__sport = sport
        self.__days = () if days is None else days
        self.__parks = parks
        # set current year and month to yearmonth if None
        if yearmonth is None:
            today = datetime.date.today()
            if today.day >= 22:
                yearmonth = today + datetime.timedelta(days=10)
            else:
                yearmonth = today
        self.__yearmonth = yearmonth.replace(day=1)
        self.__displayNo = "prwbb7000"
        if sport is not None and self.__parks is None:
            self.__displayNo = "prwbb6000"
        search_params = self.__build_serach_params()
        self.__request_body =  self.__dict_to_str(search_params, "=", "&")

    @staticmethod
    def current_yearmonth():
        today = datetime.date.today()
        ten_days = datetime.timedelta(days=10)
        if today.day >= 22:
            return (today + ten_days)
        else:
            return today

    def __create_bit_flag_list(self, length, flag_positions):
        flag_list = []
        for i in range(length):
            flag_list.append(0)
            if flag_positions.count(i) > 0:
                flag_list[-1] = 1
        return flag_list
        

    def __build_serach_params(self):
        p = copy.copy(self.__DEFAULT_SEARCH_PARAMS)
        p['displayNo'] =  self.__displayNo
        # set date related parameters.
        date = self.__yearmonth.strftime("%Y%m%d")
        p['dispWeekNum'] = len(self.__days)
        p['dispWeek'] = self.__create_bit_flag_list(
                             len(p['dispWeek']), self.__days)
        p['dispMonth'] = self.__yearmonth.month
        p['dispYMD'] = date
        p['selectM'] = self.__yearmonth.month
        p['selectYMD'] = date
        if self.__sport != None:
            p['selectPpsCd'] = self.__sport.value
        if self.__parks != None:
            parks = []
            for park in self.__parks:
                parks.append(park.number)
            p['bldBtnStat'] = self.__create_bit_flag_list(
                                   len(p['bldBtnStat']), parks)
        return p

    def __dict_to_str(self, params, kv_delimiter, item_delimiter):
        c = ""
        i = 0
        for k, v in params.items():
            if i != 0:
                c = c + item_delimiter
            if isinstance(v, list): 
                c = c + item_delimiter.join(k+"="+str(v2) for v2 in v)
            else:
                c = c + k+"="+str(v)
            i = i + 1
        return c

    @property
    def content(self):
        return self.__request_body

    def __str__(self):
        return self.__request_body

if __name__ == '__main__':
    from sport import Sport
    from park import Park
    from service import Service
    m = Service.get_months()[0]
    rb = RequestBody(yearmonth=None, days=(5,6,7))
    print(rb.content)
    rb = RequestBody(yearmonth=None, days=(5,6,7), sport=Sport.tennis_omni )
    print(rb.content)
    park = Park(Sport.tennis_omni, 1, '公園')
    rb = RequestBody(yearmonth=None, days=(5,6,7), play=play, parks=[park])
    print(rb)
