from modules.statemanager import StateManager
from modules.app import StoreApp

from states.start import StartState
from states.setup import SetupState
from states.hold import HoldState
from RPi import GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

app = StoreApp()

''' StateManager is basic State machine, which will control
different states of our app. This mainly affects LCD-screen and RFID as
REST-server is in different thread '''
sm = StateManager(app)
sm.add_state(StartState(name='start'))
sm.add_state(SetupState(name='setup'))
sm.add_state(HoldState(name='hold'))
# sm.add_state(PayState(name='pay'))
# sm.add_state(ThankState(name='thank'))
# sm.add_state(AddMoneyState(name='addmoney'))
app.start(sm)
