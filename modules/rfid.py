'''
RFID module (placeholder)

This module will be runned at the background and it will read and write to RFID tags
'''
from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522

class Rfid():
    def __init__(self):
        self.rfid = SimpleMFRC522()

    def write(self, text):
        self.rfid.write(text)

    def read(self):
        id, text = self.rfid.read()
        return id, text
