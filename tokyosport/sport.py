class Sport:

    baseball = 1011
    baseball_mini = 1012
    tennis_hard = 2021
    tennis_omni = 2023
    soccer = 3031
    soccer_mini = 3032

    def __init__(self, id, name, park_mapper):
        self.__id = id
        self.__name = name
        self.__park_mapper = park_mapper

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    def get_parks(self):
        return self.__park_mapper.retrieve(self)

    def __eq__(self, other):
        if other is None:
            return False
        if self.id != other.id:
            return False
        return True
