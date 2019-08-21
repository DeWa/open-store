from modules.screen import Screen
from modules.rfid import Rfid


class StoreApp():

    def __init__(self):
        self.screen = Screen()
        self.rfid = Rfid()
