# # Create a Class
# class Angka:
#   jumlah = 8 # Property

# a = Angka() # Object 
# print(a.jumlah)
# b = Angka() # Object 
# print(b.jumlah)

# # Custom __init__()
# class Person:
#   def __init__(self, name, age, score):
#   # initialisasi property
#     self.name = name
#     self.age = age
#     self.score = score

#   def greet(self):
#     print("Halo, " + self.name + "!")

# # Object
# p1 = Person("Cecep", 20, 95)
# p2 = Person("Budi", 25, 80)

# print(p1.name)
# print(p1.age)
# print(p1.__dict__)
# print(p2.__dict__)

# p1.greet()
# p2.greet()


# Inheritance (OOP)
class Animal: #parent class
  def __init__(self, name, age):
    # Attribut
    self.name = name 
    self.age = age

# Method
  def greet(self):
    print("Hello!")

class cat(Animal): # Child class
  def __init__(self, name, age, color, weight):
      super().__init__(name, age)
      self.color = color
      self.weight = weight

class Dog(Animal): # Child class
  def __init__(self, name, age, types):
      super().__init__(name, age)
      self.types = types

    # Animal
  # Dog    Cat
