class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        

    def __str__(self):
        return str(self.value)

num1 = Number(10)
num2 = Number(20)
num3 = Number(30)


result = num1 + num2 + num3  

print("Sum of three numbers:", result)
