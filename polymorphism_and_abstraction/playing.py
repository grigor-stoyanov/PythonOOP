def start_playing(obj):
    print(obj.play())

class Guitar:
    def play(self):
        return 'Playing guitar'
g = Guitar()
start_playing(g)
class Children:
    def play(self):
        return "Children are playing"
piano = Children()
start_playing(piano)