from modules.view import View
from time import sleep


class StartView(View):

    def run(self):
        self.app.screen.write('Open-store\nv. 0.0.1')
        sleep(2)
        self.app.screen.write('(c) Joonas Reinikka')
        sleep(2)
        self.vm.change_state('hold')

        return self
