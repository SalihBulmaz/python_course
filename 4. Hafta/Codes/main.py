

# class Dog:
#     def __init__(self, name, age, race):
#         self.name = name
#         if age < 1 or type(age) != "<class 'int'>":
#             raise ValueError
#         else:
#             self.age = age
#         self.race = race

#     def bark(self):
#         if self.race == 'Turk':
#             print('Hav Hav')
#         else:
#             print('Woff Woff')


# other_dog = Dog('Tommy', 2, 'German')
# my_dog = Dog('Griffin', -1, 'Turk')

# my_dog.bark()
# other_dog.bark()


# from math import pi
# class Sphere:
#     def __init__(self, radius):
#         self.radius = radius

#     def volume(self):
#         return (4/3) * (self.radius) ** 3 * pi


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return self.radius**2*pi

#     def perimeter(self):
#         return 2 * pi * self.radius


# # my_sphere = Sphere(3)
# # print(my_sphere.volume())


# class Cylinder:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def volume(self):
#         return self.base.area() * self.height

#     def area(self):
#         return 2 * self.base.area() + self.height * self.base.perimeter()


# base = Circle(3)
# cylinder = Cylinder(base, 7)
# print('Cylinders volume:', cylinder.volume())
# print('Cylinders area:', cylinder.area())

# class Employee:
#     def __init__(self, name, surname, age, salary):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.salary = salary

#     def __str__(self):
#         return self.full_name

#     def introduce(self):
#         print(f"I'm {self.name} {self.surname}, I'm {self.__age} years old")

#     @property
#     def full_name(self):
#         return self.name + ' ' + self.surname

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self, age):
#         if age < 18:
#             raise ValueError
#         else:
#             self.__age = age

#     @property
#     def email(self):
#         return self.name.lower() + '.' + self.surname.lower() + '@email.com'


# workers = list()
# workers.append(Employee('Tom', 'Hanks', 45, 4000))
# workers.append(Employee('Jack', 'Hjalmarch', 35, 3500))
# workers.append(Employee('Karen', 'Columbus', 30, 2500))

# for empl in workers:
#     print(empl.full_name, empl.email)
