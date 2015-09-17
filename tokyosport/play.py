from park_mapper import ParkMapper
class Play:

    BASEBALL = 1011
    BASEBALL_MINI = 1012
    TENNIS_HARD = 2021
    TENNIS_OMNI = 2023
    SOCCOR = 3031
    SOCCOR_MINI = 3032

    PLAYS = {BASEBALL: "野球"
             , BASEBALL_MINI: "野球（小）"
             , TENNIS_HARD: "テニス（ハード）"
             , TENNIS_OMNI: "テニス（人工芝）"
             , SOCCOR: "サッカー・ホッケ"
             , SOCCOR_MINI: "サッカー（小）"}

    def __init__(self, code):
        self.__code = code
        self.__name = self.PLAYS[self.__code]
        self.__parks = None

    @property
    def code(self):
        return self.__code

    @property
    def name(self):
        return self.__name

    @property
    def parks(self):
        if self.__parks == None:
            self.__parks = ParkMapper.find_by_play(self)
        return self.__parks


    def __str__(self):
        return self.__name

if __name__ == '__main__':
    p = Play(Play.BASEBALL)
    print(p.code)
    print(p.name)
    for park in p.parks:
        print(park.name)

