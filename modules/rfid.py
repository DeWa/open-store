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

    def write(self):
        try:
            text = input('New data:')
            print("Now place your tag to write")
            self.rfid.write(text)
            print("Written")
        finally:
            GPIO.cleanup()

    def read(self):
        while True:
            try:
                id, text = self.rfid.read()
                print(id)
                print(text)
            finally:
                GPIO.cleanup()
