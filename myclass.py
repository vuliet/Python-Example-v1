# Định nghĩa class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi.")

# Tạo object từ class
person1 = Person("Alice", 25)
person1.introduce()
