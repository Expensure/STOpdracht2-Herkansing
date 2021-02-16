from statemachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

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
    if sensor == on:
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
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Python_state", python_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Start")
    m.run("Python is great")
    m.run("Python is easy")
    m.run("Perl is hard")