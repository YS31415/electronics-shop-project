import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        if len(name) > 10:
            print('Длина наименования товара превышает 10 символов.')
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        class_name = str(self.__class__)
        class_name = class_name.split('.')[1].strip(">'")
        class_name = class_name.capitalize()
        return f"{class_name}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        self.__name = name
        return self.__name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls, path):
        '''класс - метод, инициализирующий экземпляры класса Item
            данными из файла src / items.csv'''
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                product = Item(row['name'], row['price'], row['quantity'])
                Item.all.append(product)
    @staticmethod
    def string_to_number(string):
        return int(float(string))

