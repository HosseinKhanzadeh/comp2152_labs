import random

class Heart:  # new*
    def __init__(self):  # new*
        self.bpm = 72

    def beat(self):  # new*
        print("Lub-dub")
        self.bpm = random.randint(70, 75)

    def __str__(self):  # new*
        return f"Heart is beating at {self.bpm}bpm."

    def __eq__(self, other):
        return self.bpm == other.bpm