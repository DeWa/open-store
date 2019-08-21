class State(object):
    def __init__(self, name):
        self.name = name
        self.sm = None
        self.app = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
