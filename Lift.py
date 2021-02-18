class Elevator():
    def __init__(self, speed, level, wanted_list):
        self.speed = speed  # Hoeveel meter/seconde
        self.height = 6  # Totale lengte van de lift in meter
        self.level_amount = 3  # Aantal etages
        self.level = level  # Begin etage
        self.inside = 0  # Aantal mensen in de lift
        self.destination_list = wanted_list
        self.sensor = False # Iemand loopt op sensor
        self.active = True # Lift is aan
        self.start_state = "closed"  # Begin state
        self.next_state = "closed"  # Bedoelde volgende state als waarden in init hetzelfde blijven.
        self.level_dictionary = self.level_dict(self.height, self.level_amount)  # Dictionary van alle etages en hun hoogte daarbij.

    def get_level(self):
        return None

    def set_destinations(self,inputs):
        return None

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

