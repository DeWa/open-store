from modules.state import State


class HoldState(State):

    def run(self):
        self.app.screen.write('Waiting for input...', 0)
