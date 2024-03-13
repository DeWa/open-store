import logging


class StateManager(object):
    def __init__(self, app):
        self.states = dict()
        self.app = app

    def add_state(self, state):
        state.sm = self
        state.app = self.app
        self.states[state.name] = state

    def change_state(self, new_state):
        try:
            return self.states[new_state].run()
        except KeyError:
            logging.error('State %s not found!' % new_state)
            return None

