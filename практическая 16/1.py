"""
Создайте класс "Машина" с атрибутами "марка", "модель" и "год выпуска".
Напишите метод, который выводит информацию о машине в формате "Марка:
марка, Модель: модель, Год выпуска: год".

блок 2:Создайте класс "Автомобиль", который содержит информацию о марке, модели и
годе выпуска. Создайте класс "Грузовик", который наследуется от класса
"Автомобиль" и содержит информацию о грузоподъемности. Создайте класс
"Легковой автомобиль", который наследуется от класса "Автомобиль" и содержит
информацию о количестве пассажиров

блок 3:Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
Использовать модуль pickle для сериализации и десериализации объектов Python в
бинарном формате.
"""

import pickle

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"Бренда: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}"
#сохранение в файл
def save_def(filename, obj):
    with open(filename, 'wb') as f:
        pickle.dump(obj, f)
#подгрузка объекта из файла 
def load_def(filename):
    with open(filename, 'rb') as f:
        obj = pickle.load(f)
    return obj
#экземпляры
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 1967)

cars = [car1, car2, car3]
save_def('cars.pickle', cars)

loaded_cars = load_def('cars.pickle')

for car in loaded_cars:
    print(car.car_info())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"Бренда: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}"

class Truck(Car):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)
        self.load_capacity = load_capacity

    def truck_info(self):
        return f"{self.car_info()}, Грузоподъемность: {self.load_capacity} т"

class PassengerCar(Car):
    def __init__(self, brand, model, year, num_passengers):
        super().__init__(brand, model, year)
        self.num_passengers = num_passengers

    def passenger_car_info(self):
        return f"{self.car_info()}, Количество пассажиров: {self.num_passengers}"
    
truck = Truck("Volvo", "FH16", 2019, 42)

print(truck.truck_info())

passenger_car = PassengerCar("Mercedes-Benz", "S-Class", 2021, 5)

print(passenger_car.passenger_car_info())
