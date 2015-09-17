class Slot:
    
    def __init__(self, park, start, end, open_count):
        self.__park = park
        self.__start = start
        self.__end = end
        self.__open_count = open_count 
        self.__hours = None

    @property
    def park(self):
        return self.__park

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    @property
    def open_count(self):
        return self.__open_count

    @property
    def hours(self):
        if self.__hours != None:
            return self.__hours
        t = self.end - self.start
        return int(t.seconds / 60 / 60)
    
    @property
    def is_available(self):
        if self.open_count > 0:
            return True
        return False

    def set_open_count(self, open_count):
        self.__open_count = open_count

    def reserve(self):
        """reserve this slot
        
        Login the system with given id/pass and reserve this slot.

        Raises:
            AssertionError: if this slot is not avaliable.
        """
        assert self.is_available() is True, "this slot is not available"
         

    def cancel(self):
        """ cancel reservation for this slot
        """
        pass
         
if __name__ == '__main__':
    from datetime import datetime
    from play import Play
    from park import Park
    a = Slot(Park(Play(Play.TENNIS_OMNI), 'kouen', 1)
                  , datetime.today().replace(hour=11)
                  , datetime.today().replace(hour=13)
                  , True)
    print(str(a.hours))
    print(str(a.is_available))
