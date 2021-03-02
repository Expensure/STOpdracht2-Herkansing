class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.time = 0

    def add_state(self, name, handler, end_state=False ):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        while True:
            newState, cargo = handler(cargo)
            print(f"reached {newState} within {cargo}")
            if newState.upper() in self.endStates:
                break
            else:
                handler = self.handlers[newState.upper()]

