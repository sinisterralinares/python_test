# Basic class
class Presenter:
    def __init__(self, name):
        # Constructor
        self.name = name

    def say_hello(self):
        # method
        print("Hello, " + self.name)


presenter = Presenter("Chris")
presenter.name = "Christopher"
presenter.say_hello()

# Property Class
class Presenter:
    def __init__(self, name):
        # Constructor
        self.name = name  # Property

    @property
    def name(self):
        print("Retrieving name...")
        return self.__name  # Getter

    @name.setter
    def name(self, value):
        # cool validation here
        print("Validating name...")
        self.__name = value  # Setter


presenter = Presenter("Chris")
presenter.name = "Christopher"
print(presenter.name)
