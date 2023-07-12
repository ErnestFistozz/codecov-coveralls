class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.last_name = surname

    @property
    def name(self) -> str:
        return self.name
    
    @property
    def surname(self) -> str:
        return self.last_name