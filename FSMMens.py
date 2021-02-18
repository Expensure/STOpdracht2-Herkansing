from statemachine import StateMachine
import random
class Human:
    entrancetime = random.randint(2,3)
    def __init__(self, start_state: str, next_state: str, level, input):
        self.start_state = "outside"
        self.next_state = "walkin_state"
        self.input = wanted_etage()
        self.current_level = current_etage()



    def outside_state(IsLiftHere,ButtonPressed):
        if IsLiftHere and ButtonPressed:
            new_state = "walk_in"
        else:
            new_state = "outside"
        return new_state

    def walkin_state():
        sensorLift = True
        new_state = "inside"
        return new_state

    def inside_state(ButtonPressed):
        selectButton
        #Gebruik button pressed later om voorrang te geven naar etage
        if FromEtage != ThisEtage and DoorOpen and wantedEtage:
            new_state = "walk_out"
        else:
            new_state = "inside"
        return new_state

    def walkout_state():
        sensorLift = True
        new_state = "outside_done"
        return new_state

    if __name__== "__main__":
        FSM = StateMachine()
        FSM.add_state("outside", outside_state,)
        FSM.add_state("walk_in", walkin_state)
        FSM.add_state("inside", inside_state)
        FSM.add_state("walk_out", walkout_state())
        FSM.set_start("outside")