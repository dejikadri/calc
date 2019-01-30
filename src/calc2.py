

class Calc():
    def add(num1, num2):
        if not isinstance(num1, int) and not isinstance(num2, int):
            return 'Invalid input'

        else:
            return num1 + num2

