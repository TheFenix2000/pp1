class University():
    def __init__(self):
        self.name = "UEK"
    def get_name(self):
        print(self.name)
    def set_name(self, newName):
        self.name = newName

university = University()
university.get_name()
university.set_name("Uniwersytet Ekonomiczny")
university.get_name()