from statemachine import StateMachine
from FSMMens import Human
HumanEntity1 = Human

class Elevator():
    def __init__(self, speed, level, wanted_list):
        self.speed = 3
        self.height = 18
        self.level_amount = 6
        self.level = 0
        self.wanted_list = []
        self.start_state = "closed"
        self.next_state = "open"
        self.level_dict = level_dict()
    def level_list(self, height,level_amount):
        return None

    def closed_state(input,location):
        if input == outside_button:
            if outside_button(etage) != location:
                newstate = "move_floor"
            else:
                newstate = "open"
        elif input == inside_button:
            newstate = "moving"
        elif input == stop:
            newstate = "stop"
        else:
            newstate = "closed"
        return (newState, location)

    def move_state(button_input, location):
        if button_input == location:
            newstate = "open"
        else:
            newstate = "moving"
        return newstate, location

    def open_state(sensor):
        if sensor == on:
            newstate = "open"
            # Addtime
        else:
            newstate = "closing"


    def closing_state(sensor):
        if sensorLift:
            newstate = "open"
            #Addtime
        else:
            newstate = "closed"

    def stop_state(input):
        if input == stop:
            newstate = "stop"
        elif input == turnmeonpls:
            newstate = "closed"


    if __name__== "__main__":
        FSM = StateMachine()
        FSM.add_state("closed", closed_state)
        FSM.add_state("moving", move_state)
        FSM.add_state("open", open_state)
        FSM.add_state("closing", closing_state())
        FSM.add_state("stop", end_state=True)
        FSM.set_start("closed")