def add_farewell(cls):
    def farewell(self):
        print(f"Goodbye, {self.__class__.__name__}...")
    cls.farewell = farewell
    return cls

@add_farewell
class My_Cat:
    pass

obj = My_Cat()
obj.farewell()

