'''
RFID module (placeholder)

This module will be runned at the background and it will read and write to RFID tags
'''

import threading


class Rfid():
    def __init__(self):
        self.input_thread = threading.Thread(target=self.read_value)
        self.input_thread.start()

    def read_value(self):
        print("Listening RFID")
        while True:
            _in = input()
            print("received input: " + _in)
