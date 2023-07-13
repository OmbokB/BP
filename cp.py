#syntax to declare functions
def function_name(arguments):
    #body
    return

def write():
    print("Hello world")
write()                                     #call the function


def multiplication(a, b):
  
    c = a * b
    print('Product:', c)
multiplication(8, 9)

def age(b, c):
    ag = c - b
    print('age:', ag)
age(int(input("year of birth: ")), int(input("Current year: ")))
 
def age(b, c):
    ag = c - b
    return ag
result = age(2002, 2021)
print('age:', result)
    
def div(num, den):
    fraction = num / den
    print("fraction:", fraction)
div(float(input("Enter numerator: ")), float(input("denominator: ")))

# b = int(input("year of birth: "))
# Y = int(input("Current year: "))
# age = Y - b
# print(int(age))




