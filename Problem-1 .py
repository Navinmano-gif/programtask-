class Calculator:
    def calculate(self, a, b, operation):
        operations = {
            "add": lambda x, y: x + y,
            "sub": lambda x, y: x - y,
            "mul": lambda x, y: x * y,
            "div": lambda x, y: x / y
        }

      
        
        if operation in operations:
            return f"{operation.replace('add','Addition').replace('sub','Subtraction').replace('mul','Multiplication').replace('div','Division')}: {operations[operation](a, b)}"
        else:
            return "Invalid Operation"


calc = Calculator()
print(calc.calculate(10, 5, "add"))
print(calc.calculate(10, 5, "sub"))
print(calc.calculate(10, 5, "mul"))
print(calc.calculate(10, 5, "div"))