from session import Session
from request import Request
from client import Client
import re
import datetime

class Service:

    def get_months():
        return Client.request_months()

if __name__ == '__main__':
    months = Service.get_months()
    for month in months:
        print("month: " + str(month))
