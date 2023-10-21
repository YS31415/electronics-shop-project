from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        if number_of_sim <= 0:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.number_of_sim = number_of_sim


    def __repr__(self):
        class_name = str(self.__class__)
        class_name = class_name.split('.')[1].strip(">'")
        class_name = class_name.capitalize()
        return f"{class_name}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        return self.quantity + other.quantity
