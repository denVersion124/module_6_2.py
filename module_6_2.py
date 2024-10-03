class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, model: str, engine_power: int, color: str, owner: str):
        self.owner = owner  # Атрибут владельца
        self.__model = model  # Атрибут модели (инкапсулированный)
        self.__engine_power = engine_power  # Атрибут мощности двигателя (инкапсулированный)
        self.__color = color  # Атрибут цвета (инкапсулированный)

    def get_model(self) -> str:
        """Возвращает модель транспорта."""
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        """Возвращает мощность двигателя."""
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        """Возвращает цвет транспорта."""
        return f"Цвет: {self.__color}"

    def set_color(self, new_color):
        if new_color not in Vehicle.__COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {new_color}")
        else:
            self.__color = new_color

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f"Владелец: {self.owner}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, model, engine_power, color, owner):
        super().__init__(model, engine_power, color, owner)

    def get_passengers_limit(self):
        return Sedan.__PASSENGERS_LIMIT


vehicle1 = Sedan('Toyota Mark II', 500, 'blue', "Fedos")
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
