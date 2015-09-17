class Park:

    def __init__(self, play, name, number):
        self.__play = play
        self.__name = name
        self.__number = number

    @property
    def play(self):
        return self.__play

    @property
    def name(self):
        return self.__name

    @property
    def number(self):
        return self.__number

    @property
    def availability(month, days=(5,6,7)):
        pass

    def __str__(self):
        return self.name

if __name__ == '__main__':
    from play import Play
    p = Park(Play(Play.TENNIS_OMNI), 1, 'kouen')
    print(p.play)
    print(p.name)
    print(p.number)

