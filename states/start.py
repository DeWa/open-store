from modules.state import State


class StartState(State):

    def run(self):
        self.app.screen.write('Open-store', 0)
        self.app.screen.write('v. 0.0.1', 0)
        self.app.screen.write('(c) Joonas Reinikka', 0)
        self.sm.change_state('hold')

        return self
