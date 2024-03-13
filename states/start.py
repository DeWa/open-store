from modules.state import State
from time import sleep


class StartState(State):

    def run(self):
        self.app.screen.write('Open-store\nv. 0.0.1')
        sleep(2)
        self.app.screen.write('(c) Joonas Reinikka')
        sleep(2)
        self.sm.change_state('hold')

        return self
