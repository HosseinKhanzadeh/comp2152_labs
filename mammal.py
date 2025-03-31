from heart import Heart

class Mammal:  # new*
    def __init__(self, age):  # new*
        self.age = age
        self.heart = Heart()

    def speak(self):  # new*
        print("Grr...")

    def __str__(self):  # new*
        return f"Mammal is {self.age} years old."
