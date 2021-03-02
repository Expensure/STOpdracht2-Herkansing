import simpy
import random
class Elevator(object):
    def __init__(self, env):
        self.speed = 2  # Hoeveel meter/seconde
        self.height = 6  # Totale lengte van de lift in meter
        self.level_amount = 3  # Aantal etages
        self.level = 0  # Begin etage
        self.inside = 0  # Aantal mensen in de lift
        self.destination_list = []
        self.destination = self.set_destinations()
        self.sensor = False # Iemand loopt op sensor
        self.active = True # Lift is aan
        self.start_state = "closed"  # Begin state
        self.next_state = "closed"  # Bedoelde volgende state als waarden in init hetzelfde blijven.
        self.level_dictionary = self.level_dict(self.height, self.level_amount)  # Dictionary van alle etages en hun hoogte daarbij.
        self.env = env
        self.action = env.process(self.run())
    def get_level(self):
        return None

    def find_duration(self):
        current = self.level_dictionary[self.level]
        destination = self.level_dictionary[self.destination]
        if current > destination:
            return (current-destination) / self.speed
        return (destination-current) / self.speed

    def set_destinations(self):
        # For every human
            # If any human in inside state:
                # Get wanted_list from all humans
                # Go to closest from this list
                # If elevator meets another current_etage:
                    # Go there first
            # Else
                # Get current_etages from all humans
                # Go to closest from this list
        return random.randint(0,2)

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
            print(f'Elevator starts moving at %d moving from {self.level} to {self.destination}' % self.env.now)
            move_duration = self.find_duration()
            self.level = self.destination
            self.destination = self.set_destinations()
            yield self.env.process(self.charge(move_duration))

            print('Elevator starts opening at %d' % self.env.now)
            door_duration = 2
            yield self.env.timeout(door_duration)

            print(f'Elevator is open at %d' % self.env.now)
            open_duration, total_open_duration = 10,10
            while open_duration < 0:
                if open_duration < 3 and self.sensor == True:
                    total_open_duration += 5-open_duration
                    open_duration = 5
                    self.sensor = False
            total_open_duration+= 5
            yield self.env.process(self.charge(total_open_duration))

            print('Elevator starts closing at %d' % self.env.now)
            door_duration = 2
            yield self.env.timeout(door_duration)

    def charge(self, duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
Ele = Elevator(env)
env.run(until=80)