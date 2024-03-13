from modules.state import State


class HoldState(State):
    def run(self):
        self.app.screen.write('Waiting for input...')
        print("Valmis ottamaan vastaan")
        self.app.rfid.read()
