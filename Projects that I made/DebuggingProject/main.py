class ageCalculate:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def increaseAge(self):
        self.age += 1

    def decreaseAge(self):
        self.age -= 1

    def __str__(self):
        return f"{self.name} is {self.age} years old!"


alperen = ageCalculate(19, "Adem Alperen")
for i in range(alperen.age):
    alperen.decreaseAge()
alperen.decreaseAge()
print(alperen)
