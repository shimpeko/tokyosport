from enum import Enum

class Sport(Enum):

    baseball = 1011
    baseball_mini = 1012
    tennis_hard = 2021
    tennis_omni = 2023
    soccer = 3031
    soccer_mini = 3032

if __name__ == '__main__':
    for s in Sport:
        print(s)

