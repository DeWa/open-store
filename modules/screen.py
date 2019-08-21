''' 
Screen module (placeholder)

Controls LCD-screen
'''


class Screen:

    def __init__(self):
        pass

    def write(self, text, line=0):
        print('\033[94m%s\033[0m' % text)
