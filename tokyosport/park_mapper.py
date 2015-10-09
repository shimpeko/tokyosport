from park import Park
from slot_mapper import SlotMapper
import re

class ParkMapper:

    def __init__(self, client):
        self.__client = client
        self.__po = re.compile("(公園|森|地)(Ａ|Ｂ|Ｃ|\s|$)")

    def retrieve(self, sport):
        response, content = self.__client.request_parks(sport)
        n = 1
        parks = []
        for line in content.decode('shift_jis').splitlines():
            if self.__po.search(line) != None:
                parks.append(Park(sport, n, line.strip()
                             , SlotMapper(self.__client)))
                n = n + 1
        return parks

if __name__ == '__main__':
    from sport import Sport
    from client import Client
    pm = ParkMapper(Client())
    for park in pm.find_by_play(Sport.tennis_omni):
        print(str(park.number) + park.name)
