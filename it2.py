##class MyClass:
##    def __init__(self, name):
##        self.name = name
##
##    def __str__(self):
##        return f"Экземпляр класса MyClass с именем {self.name}"
##
##    def __del__(self):
##        print(f"Экземпляр класса MyClass с именем {self.name} удален")
##
##    def __getattr__(self, item):
##        return f"Метод/атрибут '{item}' не найден у экземпляра"
##
##    def __setattr__(self, name, value):
##        print(f"устанавливаем значение {value} для атрибута (name)")
##        super().__setattr__(name, value)
##
##
### Создание объекта класса MyClass
##obj = MyClass("example")
##
### Вывод информации об объекте при использовании str()
##print(str(obj))
##
### Доступ к несуществующему атрибуту через __getattr__
##print(obj.some_attribute)
##
### Изменение атрибута с использованием __setattr__
##obj.new_attribute = 10
##
###Удаление объекта (вызовется_del_)
##del obj







class Cafe:
    def __init__(self, cafe_name, cafe_type):
        self.cafe_name = cafe_name
        self.cafe_type = cafe_type
    
    def describe_cafe(self):
        print(f"Cafe name: {self.cafe_name}")
        print(f"Cafe type: {self.cafe_type}")
    
    def open_cafe(self):
        print("The cafe is now open.")

    def buy_a_maid(self):
        print("Congratulations, you bought a maid, now you can...")

    def pogladit(self):
        print("Vi ee pogladili, vam nravitsa:)")

# Создаем экземпляр класса Cafe
cafe = Cafe("My Cafe", "Neko made cafe")

# Выводим атрибуты по отдельности
print("Cafe name:", cafe.cafe_name)
print("Cafe type:", cafe.cafe_type)

# Вызываем методы
cafe.describe_cafe()
cafe.open_cafe()
g = int(input("Хотите купить neko горничную? Yes(1)/no(2)"))
if g == 1:
    cafe.buy_a_maid()
else:
    print("zra ti tak")

z = int(input("hotite pogladit svou neko gornichnyu? Yes(1)/no(2)"))
if z == 1:
    cafe.pogladit()
else:
    print("zra ti tak")




##class Vehicle:
##    def __init__(self, make, model):
##        self.make = make
##        self.model = model
##
##    def display_info(self):
##        print(f"Make: {self.make}")
##        print(f"Model: {self.model}")
##
##
##class Car(Vehicle):
##    def __init__(self, make, model, num_wheels):
##        super().__init__(make, model)
##        self.num_wheels = num_wheels
##
##    def display_info(self):
##        super().display_info()
##        print(f"Number of wheels: {self.num_wheels}")
##
##
##class Motorcycle(Vehicle):
##    def __init__(self, make, model, num_wheels):
##        super().__init__(make, model)
##        self.num_wheels = num_wheels
##
##    def display_info(self):
##        super().display_info()
##        print(f"Number of wheels: {self.num_wheels}")
##
##
### Создаем объекты Car и Motorcycle
##car = Car("Mercedes", "Maybach", 4)
##motorcycle = Motorcycle("Ducati", "SuperleggeraV4", 2)
##
### Вызываем метод display_info для каждого объекта
##print("Car:")
##car.display_info()
##print("\nMotorcycle:")
##motorcycle.display_info()





















































