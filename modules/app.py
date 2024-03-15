from modules.screen import Screen
from modules.rfid import Rfid


class StoreApp():
    viewmanager = None

    def __init__(self):
        self.screen = Screen()
        self.rfid = Rfid()

    def start(self, vm):
        self.viewmanager = vm
        self.viewmanager.change_view('hold')
