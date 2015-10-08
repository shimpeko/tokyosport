from sport import Sport

class Park:

    def __init__(self, sport, seq, name):
        self.__sport = sport
        self.__seq = seq
        self.__name = name

    @property
    def sport(self):
        return self.__sport

    @property
    def seq(self):
        return self.__seq

    @property
    def name(self):
        return self.__name

