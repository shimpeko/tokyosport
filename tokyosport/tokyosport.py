from client import Client
from day import Day
from sport import Sport
from slot import Slot

class TokyoSport:

    def __init__(self):
        pass

    def get_months(self):
        return Client.request_months()

    def get_days(self):
        return list(Day)

    def get_sports(self):
        return list(Sport)

    def get_parks(self, sport):
        pass

    def get_slots(self, sport, month, days, parks):
        pass

    def get_available_slots(self, sport, month, days, parks):
        pass

if __name__ == '__main__':
    ts = TokyoSport()
    print(ts.get_months())
    print(ts.get_days())
    print(ts.get_sports())
