from statemachine import StateMachine
import random
from FSMLift import Elevator

Ele = Elevator(3, 0, [])
get_level = list((Ele.get_dict()).keys())


class Human:
    entrancetime = random.randint(2, 3)

    def __init__(self):
        self.start_state = "outside"
        self.next_state = "walkin_state"
        self.current_level = self.current_etage(get_level)
        self.input = self.wanted_etage(get_level)

    def current_etage(self, get_level):
        return int(random.choice(get_level))

    def get_current(self):
        return self.current_level

    def wanted_etage(self, get_level):
        temp_level = get_level
        new = self.get_current()
        temp_level.remove(new)
        return random.choice(temp_level)

    def get_destination(self):
        return self.input




