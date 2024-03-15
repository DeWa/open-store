from modules.viewmanager import ViewManager
from modules.app import StoreApp

from views.start import StartView
from views.setup import SetupView
from views.hold import HoldView

app = StoreApp()

''' ViewManager is basic state machine, which will control
different states of our app. This mainly affects LCD-screen and RFID '''
vm = ViewManager(app)
vm.add_view(StartView(name='start'))
vm.add_view(SetupView(name='setup'))
vm.add_view(HoldView(name='hold'))
app.start(vm)
