from enum import Enum

class Day(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6
    Holiday = 7

if __name__ == '__main__':
    for d in Day:
        print(d)
