from FSMMens import Human
from FSMLift import Elevator
from statemachine import StateMachine




class ElevatorFSM(Elevator):
    def closed_state(self, input, location):
        if Ele.level in Ele.destination_list:
            newstate = "open"
        elif Ele.destination_list != []:
            newstate = "move_floor"
        else:
            newstate = "closed"
        return newstate, location

    def move_state(self):
        if Ele.level in Ele.destination_list:
            newstate = "open"
        else:
            newstate = "moving"
        return newstate, Ele.level

    def open_state(self):
        Ele.destination_list.remove(Ele.level)
        Countdown = 10
        # Eigenlijk timer van tien seconden
        while Ele.sensor and Countdown < 3:
            Countdown = 5
            #Add 5 more seconds to avoid pancake
        newstate = "closing"

    def closing_state(self, sensor):
        if Ele.sensor:
            newstate = "open"
            # Addtime
        else:
            newstate = "closed"

    #def stop_state(self, input):
        #if input == stop:
            #newstate = "stop"
        #elif input == turnmeonpls:
            #newstate = "closed"

    if __name__ == "__main__":
        FSM = StateMachine()
        FSM.add_state("closed", closed_state)
        FSM.add_state("moving", move_state)
        FSM.add_state("open", open_state)
        FSM.add_state("closing", closing_state())
        FSM.add_state("stop", end_state=True)
        FSM.set_start("closed")


class HumanSFM(Human):
    def outside_state(self, IsLiftHere):
        Ele.sensor = False
        if Ele.level == Hum.get_current():
            new_state = "walk_in"
            #Add 2 tot 3 seconden
        else:
            new_state = "outside"
            #Voeg tijd toe tot lift er is.
        return new_state

    def walkin_state(self):
        Ele.sensor = True
        new_state = "inside"
        return new_state

    def inside_state(self):
        Ele.sensor = False
        Hum.input = Hum.wanted_etage(get_level)
        if Ele.move_state() == "open" and Hum.input == Ele.level:
            #Als je boven bent
            new_state = "walk_out"
        else:
            #Als wachten tot je boven bent
            new_state = "inside"
        return new_state

    def walkout_state(self):
        Ele.sensor = True
        #Geef 2-3 seconden tijd
        new_state = "Done"
        return new_state

    if __name__ == "__main__":
        FSM = StateMachine()
        FSM.add_state("outside", outside_state, )
        FSM.add_state("walk_in", walkin_state)
        FSM.add_state("inside", inside_state)
        FSM.add_state("walk_out", walkout_state())
        FSM.add_state("Done", end_state= True)
        FSM.set_start("outside")

Ele = ElevatorFSM(3, 0, [])
Hum = Human()
get_level = list((Ele.get_dict()).keys())
Ele.destination_list.append(Hum.get_current())
Ele.destination_list.append(Hum.get_destination())
if Ele.level in Ele.destination_list:
    new_state = "Yay"
else:
    new_state = "Move"