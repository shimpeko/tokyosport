from sport import Sport
from day import Day

class Park:

    def __init__(self, sport, seq, name, slot_mapper):
        self.__sport = sport
        self.__seq = seq
        self.__name = name
        self.__slot_mapper = slot_mapper

    @property
    def sport(self):
        return self.__sport

    @property
    def seq(self):
        return self.__seq

    @property
    def name(self):
        return self.__name

    def get_slots(self, month, days):
        days = [Day[d] for d in days]
        return self.__slot_mapper.retrieve(month, days, [self])
