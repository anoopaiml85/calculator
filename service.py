'''Create a simple calculator 
   - Addition
   - Substraction
   - Multiplication
   - Division
- PROBLEM SOLUTION
 - Create a class and using a constructor intialize values.
 - Create methods for adding, substracting,multiplying,dividing two numbers. 
 - Take two numbers as inputs and create an object of the class passing two numbers as parameters. '
 - Validate
 - Using the class object select which operation we want to perform using the user input. 
 - 0 - Addition,1- Substraction,2-Multiplicaiton,3 - Division
 - Print the result. 
 - Exit
'''
class Calculator():
    def __init__(self,a,b) -> None:
        self.a = a #assign to object.Class variables.Intilization
        self.b = b
    def addition(self):
        return self.a + self.b
    def substraction(self):
        return self.a - self.b  
    def multiplication(self):
        return self.a * self.b   
    def division(self):
        return self.a / self.b    



a = input ("Enter first integer: ")
b = input("Enter seconf integer: ")
a = int(a)
b=int(b)
calc = Calculator(a,b)
Operation = input( "Enter 1- Addition, 2- Sub , 3 Multiplication, 4 Division : ")
print(type(Operation))
if Operation == '1':
    output = calc.addition()
elif Operation == '2':
    output = calc.substraction()
elif Operation == '3':
    output = calc.multiplication()
elif Operation == '4':
    output = calc.division()

print(output)    

     
  
