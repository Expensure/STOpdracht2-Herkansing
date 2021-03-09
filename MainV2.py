import simpy
import random


def main(tijd):
    env = simpy.Environment()
    Ele = Elevator(env, 1)
    levellist = list(Ele.level_dictionary.keys())
    Hum1 = Human(levellist, env, Ele)
    env.run(until=tijd)
    print(f"Simulation gestopt op: {tijd}")


class Elevator(object):
    def __init__(self, env, speed):
        self.state = 0  # 0 = dicht, #1 = moving, #2 = open
        self.speed = speed  # Hoeveel meter/seconde
        self.height = 12  # Totale lengte van de lift in meter
        self.level_amount = 5  # Aantal etages
        self.level = 0  # Begin etage
        self.inside = 0  # Aantal mensen in de lift
        self.destination_list = []
        self.destination = self.set_destinations()
        self.sensor = False  # Iemand loopt op sensor
        self.active = True  # Lift is aan
        self.start_state = "closed"  # Begin state
        self.next_state = "closed"  # Bedoelde volgende state als waarden in init hetzelfde blijven.
        self.level_dictionary = self.level_dict(self.height,
                                                self.level_amount)  # Dictionary van alle etages en hun hoogte daarbij.
        self.env = env
        self.action = env.process(self.run())

    def find_duration_moving(self):
        current = self.level_dictionary[self.level]
        print(self.destination)
        destination = self.level_dictionary[self.destination]
        return (abs(destination - current)) / self.speed

    def set_destinations(self):
        if not self.destination_list:
            return None
        else:
            shortest = 100
            for i in self.destination_list:
                diff = abs((self.level - i))
                if diff < shortest:
                    shortest = diff
            return shortest

    def level_dict(self, height, level_amount):
        # Maakt een dictionary van elke etage en gebruikt de gemiddelde afstand tussen de etages)
        all_levels = []
        all_heights = []
        mean_height = height / (level_amount - 1)

        for i in range(0, level_amount):
            all_levels.append(i)
            all_heights.append(i * mean_height)
        dictionary = dict(zip(all_levels, all_heights))

        return dictionary

    def get_dict(self):
        return self.level_dictionary

    def run(self):
        while True:
            if self.destination_list:
                print(f'Elevator starts moving at %d moving from {self.level} to {self.destination}' % self.env.now)
                move_duration = self.find_duration_moving()
                self.level = self.destination
                self.destination = self.set_destinations()
                yield self.env.process(self.charge(move_duration))

                print('Elevator starts opening at %d' % self.env.now)
                door_duration = 2
                yield self.env.timeout(door_duration)

                print(f'Elevator is open at %d' % self.env.now)
                self.state = 1
                open_duration, total_open_duration = 10, 10
                while open_duration < 0:
                    if open_duration < 3 and self.sensor == True:
                        total_open_duration += 5 - open_duration
                        open_duration = 5
                        self.sensor = False
                    total_open_duration += 5
                yield self.env.process(self.charge(total_open_duration))

                print('Elevator starts closing at %d' % self.env.now)
                door_duration = 2
                yield self.env.timeout(door_duration)
                self.state = 0
                yield self.env.timeout(1)
            else:
                yield self.env.process(self.charge(1))

    def charge(self, duration):
        yield self.env.timeout(duration)


class Human(object):
    def __init__(self, level_list, env, other, walk_time=2, lives=3):
        self.level_list = level_list
        self.walk_time = walk_time
        self.lives = lives
        self.env = env
        self.level = self.set_level()
        self.destination = self.set_destination(self.level)
        self.other = other
        self.action = env.process(self.run())
        self.state = 0

    def set_level(self, destination=''):
        if destination == '':
            return random.choice(self.level_list)
        else:
            return destination

    def set_destination(self, level, destination=''):
        temp_levels = self.level_list.copy()
        if destination != '':
            temp_levels.remove(destination)
        temp_levels.remove(level)
        return random.choice(temp_levels)

    # def set_destination(self, current_level):
    # return None

    # def wachttijd(self, duration):
    # yield self.env.timeout(duration)

    # def current_etage(self, get_level):
    # return int(random.choice(get_level))

    # def get_current(self, level):
    # return level

    # def wanted_etage(self, get_level, current_level):
    # temp_level = get_level
    # temp_level.remove(self.get_current(current_level))
    # return random.choice(temp_level)

    # def get_destination(self):
    # return None
    def run(self):
        while self.lives > 0:

            self.level = self.set_level()  # mens kiest start etage.
            self.destination = self.set_destination(self.level)  # mens kiest eind etage

            print(
                f'Human presses elevator button at %d from level {self.level}.' % self.env.now)  # mens staat bij lift deur.
            self.other.destination_list.append(self.level)
            self.give_current(self.level)

            while True:

                try:
                    if self.other.state == 1 and self.level == self.other.level:  # lift is op etage mens en deur is open
                        print(f'human walks in lift at %d' % self.env.now)
                        self.state = 1
                        yield self.env.process(self.wachttijd(self.walk_time))

                        print(f'human is in lift at %d' % self.env.now)

                        self.give_destination(self.destination)

                        while True:
                            if self.other.state and self.other.level == "TODO" and self.state == 1:  # lift is op eind_etage.
                                self.state = 2
                                print(f'human walks out lift at %d' % self.env.now)
                                yield self.env.process(self.wachttijd(self.walk_time))
                                yield self.env.process(self.wachttijd(16))
                                self.lives -= 1
                                break

                            else:
                                yield self.env.process(self.wachttijd(1))  # Iedere seconde dat mens wacht op de lift.

                    else:
                        yield self.env.process(self.wachttijd(1))  # Iedere seconde dat mens wacht op de lift.

                except simpy.Interrupt:
                    self.lives -= 1
                    pass

    def give_current(self, level):
        if level not in self.other.destination_list:
            self.other.destination_list.append(level)
        return None

    def give_destination(self, dest_level):
        if dest_level not in self.other.destination_list:
            self.other.destination_list.append(dest_level)
        return None

    def wachttijd(self, duration):
        yield self.env.timeout(duration)

    def current_etage(self, get_level):
        return int(random.choice(get_level))

    def get_current(self, level):
        return level

    def wanted_etage(self, get_level, current_level):
        temp_level = get_level
        temp_level.remove(self.get_current(current_level))
        return random.choice(temp_level)

    def get_destination(self):
        return None


if __name__ == '__main__':
    main(500)