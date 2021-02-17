from statemachine import StateMachine

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
    new_state = "inside"
    return new_state

if __name__== "__main__":
    FSM = StateMachine()
    FSM.add_state("closed", closed_state)
    FSM.add_state("moving", move_state)
    FSM.add_state("open", open_state)
    FSM.add_state("closing", closing_state())
    FSM.add_state("stop", end_state=True)
    FSM.set_start("closed")