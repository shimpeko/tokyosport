from request import Request
from request_body import RequestBody
from client import Client
from park import Park
import re

class ParkMapper:

    __PARK_ACTION = "rsvWTransInstSrchMultipleAction.do"

    @staticmethod
    def find(play, name):
        for park in ParkMapper.find_by_play(play):
            if(park.name == name):
                return park
    
    @staticmethod
    def find_by_play(play):
        response, content = Client().request(play)
        n = 1
        parks = []
        po = re.compile("(公園|森|地)(Ａ|Ｂ|Ｃ|\s|$)")
        for line in content.decode('shift_jis').splitlines():
            if po.search(line) != None:
                parks.append(Park(play, line.strip(), n))
                n = n + 1
        return parks

    @staticmethod
    def find_all(session=None):
        #TODO
        pass

    @staticmethod
    def __request_parks(play):
    
         

if __name__ == '__main__':
    from play import Play
    for park in ParkMapper.find_by_play(Play(Play.TENNIS_OMNI)):
        print(str(park.number) + park.name)
    print(ParkMapper.find(Play(Play.TENNIS_HARD), '城北中央公園').name)

