from client import Client
from days import Days

class TokyoSport:

    def __init__(self):
        pass

    def get_months(self):
        return Client.request_months()

    def get_days(self):
        return list(Days)


    def get_parks(self):
        return 

if __name__ == '__main__':
    ts = TokyoSport()
    print(ts.get_months())
    print(ts.get_days())
