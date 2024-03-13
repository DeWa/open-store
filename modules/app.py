from modules.screen import Screen
from modules.rfid import Rfid


class StoreApp():
    statemanager = None

    def __init__(self):
        self.screen = Screen()
        self.rfid = Rfid()

    def start(self, sm):
        self.screen.write("testi")
        self.statemanager = sm
        self.statemanager.change_state('hold')
