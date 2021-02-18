import random
from Lift import Elevator

Ele = Elevator(3, 0, [])
get_level = list((Ele.get_dict()).keys())


class Human:
    def __init__(self):
        self.start_state = "outside"
        self.next_state = "walkin_state"
        self.current_level = self.current_etage(get_level)
        self.input = None

    def current_etage(self, get_level):
        return int(random.choice(get_level))

    def get_current(self):
        return self.current_level

    def wanted_etage(self, get_level):
        temp_level = get_level
        temp_level.remove(self.get_current())
        return random.choice(temp_level)

    def get_destination(self):
        return self.input




