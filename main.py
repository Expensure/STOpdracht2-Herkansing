from FSMMens import Human
from FSMLift import Elevator
from statemachine import StateMachine

Ele = Elevator(3, 0, [])
Hum = Human()

Ele.destination_list.append(Hum.get_current())
Ele.destination_list.append(Hum.get_destination())
if Ele.level in Ele.destination_list:
    new_state = "Yay"
else:
    new_state = "Move"


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

    def open_state(self, sensor):
        Ele.destination_list.remove(Ele.level)
        # Eigenlijk timer van tien seconden
        if sensor == on:
            newstate = "open"
            # Addtime gebaseerd op hoeveel nog binnen lopen
        else:
            newstate = "closing"

    def closing_state(self, sensor):
        if sensorLift:
            newstate = "open"
            # Addtime
        else:
            newstate = "closed"

    def stop_state(self, input):
        if input == stop:
            newstate = "stop"
        elif input == turnmeonpls:
            newstate = "closed"

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
        if Ele.level == Hum.get_current():
            new_state = "walk_in"
            #Add 2 tot 3 seconden
        else:
            new_state = "outside"
            #Voeg tijd toe tot lift er is.
        return new_state

    def walkin_state(self):
        sensorLift = True
        new_state = "inside"
        return new_state

    def inside_state(self, ButtonPressed):
        selectButton
        # Gebruik button pressed later om voorrang te geven naar etage
        if FromEtage != ThisEtage and DoorOpen and wantedEtage:
            new_state = "walk_out"
        else:
            new_state = "inside"
        return new_state

    def walkout_state(self):
        sensorLift = True
        new_state = "outside_done"
        return new_state

    if __name__ == "__main__":
        FSM = StateMachine()
        FSM.add_state("outside", outside_state, )
        FSM.add_state("walk_in", walkin_state)
        FSM.add_state("inside", inside_state)
        FSM.add_state("walk_out", walkout_state())
        FSM.set_start("outside")
