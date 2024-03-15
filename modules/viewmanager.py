import logging


class ViewManager(object):
    def __init__(self, app):
        self.views = dict()
        self.app = app

    def add_view(self, view):
        view.vm = self
        view.app = self.app
        self.views[view.name] = view

    def change_view(self, new_view):
        try:
            return self.views[new_view].run()
        except KeyError:
            logging.error('View %s not found!' % new_view)
            return None

