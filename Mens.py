import random
from Lift import Elevator
import simpy

Ele = Elevator(3, 0, [])
get_level = list((Ele.get_dict()).keys())


class Human(object):
    def __init__(self, env, other, start_etage, eind_etage, walk_time=2):
        self.walk_time = walk_time
        self.env = env
        self.other = other
        self.start_etage = start_etage
        self.eind_etage = eind_etage

        self.action = env.process(self.run())

    def run(self):
        print(
            f'human presses elevator button at %d from level {self.start_etage}.' % self.env.now)  # mens staat bij lift deur.

        # add start_etage to destinations

        while True:
            try:
                if self.other.state:  # lift is op etage mens.
                    print(f'human walks in lift at %d' % self.env.now)
                    yield self.env.process(self.wachttijd(self.walk_time))

                    print(f'human is in lift at %d' % self.env.now)

                    # add eind_etage to destinations

                    while True:
                        if self.other.state:  # lift is op eind_etage.
                            print(f'human walks out lift at %d' % self.env.now)
                            yield self.env.process(self.wachttijd(self.walk_time))

                            print(f'human is at disiard level %d' % self.env.now)
                            break

                        else:
                            yield self.env.process(self.wachttijd(1))  # Iedere seconde dat mens wacht op de lift.

                else:
                    yield self.env.process(self.wachttijd(1))  # Iedere seconde dat mens wacht op de lift.

            except simpy.Interrupt:
                pass

    def wachttijd(self, duration):
        yield self.env.timeout(duration)

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




