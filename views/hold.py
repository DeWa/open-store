from modules.view import View


class HoldView(View):
    def run(self):
        self.app.screen.write('Scan QR-code or\nbankcard')
