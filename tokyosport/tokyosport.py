from client import Client
from day import Day
from sport import Sport
from park_mapper import ParkMapper
from park import Park
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
        return [s.name for s in Sport]

    def get_parks(self, sport):
        return ParkMapper(self.__client).retrieve(Sport[sport])
            
    def get_slots(self, month, days, parks):
        yearmonth = datetime.date.today().replace(month=month)
        days = [Day[d] for d in days]
        return SlotMapper(self.__client).retrieve(yearmonth, days, parks)

    def get_available_slots(self, sport, month, days, parks):
        pass

if __name__ == '__main__':
    ts = TokyoSport()
    months = ts.get_months()
    print(months)
    print(ts.get_days())
    print(ts.get_sports())
    parks = ts.get_parks('tennis_omni')
    for p in parks:
        print(p.name)
    for s in ts.get_slots(months[0], ['Saturday', 'Sunday'], parks):
        print(s.start)


