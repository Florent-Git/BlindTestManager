from controller.controller import Controller


class HomeController(Controller):
    def __init__(self, name):
        super().__init__()
        self.__dict__['name'] = name
