import random
import simpy


class Human(object):
    def __init__(self, env, start_level, end_level, other, walk_time=2):
        self.walk_time = walk_time
        self.env = env
        self.other = other
        self.level = start_level
        self.eind_etage = end_level
        self.action = env.process(self.run())

    def run(self):
        print(
            f'Human presses elevator button at %d from level {self.level}.' % self.env.now)  # mens staat bij lift deur.

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
        return None

    def wanted_etage(self, get_level):
        temp_level = get_level
        temp_level.remove(self.get_current())
        return random.choice(temp_level)

    def get_destination(self):
        return None


env = simpy.Environment()
env.run(until=80)
