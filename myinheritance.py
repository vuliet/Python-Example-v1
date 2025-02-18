# Lớp cha
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Động vật phát ra âm thanh")

# Lớp con kế thừa từ Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} sủa gâu gâu!")

# Tạo object từ lớp con
dog = Dog("Cún")
dog.speak()
