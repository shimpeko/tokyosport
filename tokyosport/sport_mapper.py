from sport import Sport
from park_mapper import ParkMapper
import re

class SportMapper:

    def __init__(self, client):
        self.__client = client
        self.__po = re.compile('^.*\'(\d{4})\'\).*alt="(.*?)">$')

    def retrieve(self):
        r, c = self.__client.request_sports()
        link_lines = (l for l in c.decode('shift_jis').splitlines() if \
                      l.strip().startswith('<a href="javaScript:sendPpsCd'))
        sports = []
        for line in link_lines:
            ro = self.__po.match(line)
            sports.append(Sport(ro.group(1), ro.group(2)
                                , ParkMapper(self.__client)))
        return sports

if __name__ == '__main__':
    from client import Client
    sm =  SportMapper(Client())
    for s in sm.find():
        print(s.id)
        print(s.name)
