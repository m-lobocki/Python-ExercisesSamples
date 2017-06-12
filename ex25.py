# Define a class, which have a class parameter and have a same instance parameter.

class Car:
    def __init__(self, model):
        self.model = model

audi = Car('audi')
print(audi.model)