from client import Client
from day import Day
from sport import Sport
from sport_mapper import SportMapper
from park import Park
from park_mapper import ParkMapper
from slot import Slot
from slot_mapper import SlotMapper
import datetime

class TokyoSport:

    def __init__(self):
        self.__client = Client()

    def get_months(self):
        return self.__client.request_months()

    def get_days(self):
        return [d.name for d in Day]

    def get_sports(self):
        return SportMapper(self.__client).retrieve()

    def get_park(self, sport_id, sport_name):
        return Sport(sport_id, sport_name, ParkMapper(self.__client))\
               .get_parks()
            
    def get_slots(self, month, days, parks):
        slots = []
        for park in parks:
            slots.extend(park.get_slots(month, days))
        return slots

    def get_available_slots(self, sport, month, days, parks):
        pass

if __name__ == '__main__':
    ts = TokyoSport()
    months = ts.get_months()
    sports = ts.get_sports()
    for s in sports:
        print(s.name)
        for p in s.get_parks():
            print(p.name)
            for slot in p.get_slots(months[0], ['Sunday']):
                print(slot.start)

