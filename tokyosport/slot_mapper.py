from client import Client
import re
import datetime
import copy
from slot import Slot

class SlotMapper:

    _day_po = re.compile("(\d{2})/(\d{1,2})\((.+?)\)")
    _time_po = re.compile("^\s{2,}(\d{2}):(\d{1,2})")
    _slot_po = re.compile("width=\"70px\"\s+height=\"39\"")
    _open_po = re.compile("^\s+<b>(\d)</b>$")

    def __init__(self, client):
        self.__client = client

    def retrieve(self, yearmonth, days, parks):
        park_idxs = [i for i in range(len(parks))]
        slots = []
        # retrive slot by 2 parks
        for even_park_idx in park_idxs[0::2]:
            request_parks = parks[even_park_idx:even_park_idx + 2]
            response, content = self.__client.request(
                                                      parks[0].sport
                                                      , yearmonth
                                                      , days
                                                      , request_parks)
            dates = []
            time_idx = 0
            slot_idx = 0
            request_park_idx = -1
            for line in content.decode('shift_jis').splitlines():
                day_ro = SlotMapper._day_po.search(line)
                time_ro = SlotMapper._time_po.match(line)
                slot_ro = SlotMapper._slot_po.search(line)
                open_ro = SlotMapper._open_po.match(line)
                if day_ro != None:
                    ym = copy.copy(yearmonth)
                    date = ym.replace(day=int(day_ro.group(2)))
                    dates.append(date)
                if time_ro != None:
                    if time_idx == 0:
                        time_ranges = []
                        slot_idx = 0
                    t = {"hour": int(time_ro.group(1))
                         , "minute": int(time_ro.group(2))}
                    if time_idx % 2 == 0:
                        time_range = {}
                        time_range['begin'] = t
                    else:
                        time_range['end'] = t
                        time_ranges.append(time_range)
                    time_idx = time_idx + 1
                if slot_ro != None:
                    # if first slot for a park
                    if time_idx != 0:
                        time_idx = 0
                        request_park_idx = request_park_idx + 1
                    slot_count_per_day = len(time_ranges)
                    # get proper date from dates by slot_idx
                    date = dates[int(slot_idx / slot_count_per_day)]
                    # get proper time_range from time_ranges by slot_idx
                    time_range = time_ranges[slot_idx % (slot_count_per_day)]
                    begin_datetime = datetime.datetime(
                                     date.year, date.month, date.day
                                     , time_range['begin']['hour']
                                     , time_range['begin']['minute']
                                     , 0)
                    end_datetime = datetime.datetime(
                                   date.year, date.month, date.day
                                   , time_range['end']['hour']
                                   , time_range['end']['minute']
                                   , 0)
                    slots.append(Slot(request_parks[request_park_idx]
                                      , begin_datetime
                                      , end_datetime
                                      , 0))
                    slot_idx = slot_idx + 1
                if open_ro != None:
                    slots[-1].set_open_count(int(open_ro.group(1)))
        return slots
            
if __name__ == '__main__':
    from play import Play
    from park import Park
    import datetime
    client = Client()
    parks = [Park(Play(Play.TENNIS_OMNI), '日比谷公園', 1)
             , Park(Play(Play.TENNIS_OMNI), '舎人公園', 12)]
    slots = SlotMapper.find_by_parks(datetime.date.today().replace(month=6)
                                     , (5,6,7)
                                     , parks
                                     , client)
    for slot in slots:
        print(slot.park)
        print(slot.start)
        print(slot.open_count)

    park = Park(Play(Play.TENNIS_OMNI), '日比谷公園', 1)
    slots = SlotMapper.find_by_park(datetime.date.today(), (5,6,7)
                                    , park
                                    , client)
    for slot in slots:
        print(slot.park)
        print(slot.start)
