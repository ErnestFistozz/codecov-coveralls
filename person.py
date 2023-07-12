class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    @property
    def name(self) -> str:
        return self.name
    
    @property
    def surname(self) -> str:
        return self.surname

    @name.setter
    def name(self, value):
        self.name = value
    
    @surname.setter
    def name(self, value):
        self.surname = value