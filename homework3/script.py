# #ДЗ 

# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_square(self) -> int:
        return self.x * self.y
    
    def __add__(self, other) -> int:
        return self.get_square() + other.get_square()
    
    def __sub__(self, other) -> int:
        return self.get_square() - other.get_square()
    
    def __eq__(self, other) -> bool:
        return self.get_square() == other.get_square()
    
    def __ne__(self, other) -> bool:
        return self.get_square() != other.get_square()
    
    def __lt__(self, other) -> bool:
        return self.get_square() < other.get_square()
    
    def __gt__(self, other) -> bool:
        return self.get_square() > other.get_square()
    
    def __len__(self) -> int:
        return self.x + self.y
    
# rec = Rectangle(5, 5)
# rec2 = Rectangle(6, 10)

# print('Sum of squares', rec + rec2)
# print('Sub of squares', rec - rec2)
# print('length = ', len(rec))
    


#   ###############################################################################

# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму

# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
    
    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return super().__new__(cls)
    
    def __str__(self):
        return self.name + ' ' + str(self.foot_size)

    @classmethod
    def get_number_of_cinderelaas(cls):
        return cls.__count


class Prince(Human):
    def __init__(self, name: str, age: int, shoes_size: int):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def find_cinderella(self, cinderellas: list[Cinderella]) -> Cinderella | None:
        cinderella = None
        for cind in cinderellas:
            if cind.foot_size == self.shoes_size:
                cinderella = cind
        return cinderella

# cinderella1 = Cinderella('Cinderella1', 18, 38)
# cinderella2 = Cinderella('Cinderella2', 21, 39)
# prince1 = Prince('Prince1', 18, 40)
# prince2 = Prince('Prince2', 21, 39)
# print(prince2.find_cinderella([cinderella1, cinderella2]))
# print(Cinderella.get_number_of_cinderelaas())



# ###############################################################################

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:

# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))

#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
    

# для перевірки ксассів використовуємо метод isinstance, приклад:


# user = User('Max', 15)
# shape = Shape()

# isinstance(max, User) -> True
# isinstance(shape, User) -> False
    
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("The name of the book is ", self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("The name of the magazine is ", self.name)


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def add(cls, print_obj: Printable):
        if isinstance(print_obj, Printable):
            cls.__printable_list.append(print_obj)

    @classmethod
    def show_all_magazines(cls):
        for pr in cls.__printable_list:
            if isinstance(pr, Magazine):
                pr.print()
    
    @classmethod
    def show_all_books(cls):
        for pr in cls.__printable_list:
            if isinstance(pr, Book):
                pr.print()


# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))

# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()