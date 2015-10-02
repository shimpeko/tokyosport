from client import Client
from day import Day
from sport import Sport
from park import Park
from slot import Slot
import json

class TokyoSport:

    def __init__(self):
        pass

    def get_months(self):
        return Client.request_months()

    def get_days(self):
        return [d.name for d in Day]

    def get_sports(self):
        return [s.name for s in Sport]

    def get_parks(self):
        parks = []
        with open('data/park_list.json') as f:
            park_list = json.loads(f.read())
        for i, p in sorted(park_list.items()):
            parks.append(Park(i 
                              , p['name']
                              , p['baseball']
                              , p['baseball_mini']
                              , p['tennis_hard']
                              , p['tennis_omni']
                              , p['soccer']
                              , p['soccer_mini']))
        return parks

    def get_slots(self, sport, month, days, parks):
        pass

    def get_available_slots(self, sport, month, days, parks):
        pass

if __name__ == '__main__':
    ts = TokyoSport()
    print(ts.get_months())
    print(ts.get_days())
    print(ts.get_sports())
    for n in ts.get_parks():
        print(n)
