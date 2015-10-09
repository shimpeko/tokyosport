from enum import Enum

class Sport:

    baseball = 1011
    baseball_mini = 1012
    tennis_hard = 2021
    tennis_omni = 2023
    soccer = 3031
    soccer_mini = 3032

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name
