from sport import Sport

class Park:

    def __init__(self, id, name, baseball, baseball_mini, tennis_hard\
                 , tennis_omni, soccer, soccer_mini):
        self.__id = id
        self.__name = name
        self.__field_counts = {Sport.baseball: baseball
                               , Sport.baseball_mini: baseball_mini
                               , Sport.tennis_hard: tennis_hard
                               , Sport.tennis_omni: tennis_omni
                               , Sport.soccer: soccer_mini
                               , Sport.soccer_mini: soccer_mini}

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def field_counts(self):
        return self.__field_counts

    def get_slots(month, days=(5,6,7)):
        pass

    def __str__(self):
        return self.name

if __name__ == '__main__':
    p = Park(1,'kouen',1,2,3,4,5,6)
    print(p.id)
    print(p.name)
    print(p.field_counts)

