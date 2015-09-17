from request import Request
from request_body import RequestBody
from client import Client
from play import Play

class PlayMapper:

    @staticmethod
    def find_all():
        r, content = Client().request()
        plays = []
        for k in Play.PLAYS.keys():
            plays.append(Play(k))
        return plays

    @staticmethod
    def find(code):
        plays = PlayMapper.find_all()
        for play in plays:
            if(play.code == code):
                return play

if __name__ == '__main__':
    for play in PlayMapper.find_all():
        print(str(play.code) + play.name)
    print(PlayMapper.find(Play.TENNIS_HARD).name)

