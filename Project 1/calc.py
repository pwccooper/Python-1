
def say_hello():
    print("I'm a function")

def perform_sum(num1, num2):
   print('performing sum operation inside a function')
   return num1 + num2

def perform_div(num1, num2):
    if(num2 == 0):
        print("Error, can not be divided by zero")
        return 0
    else:
        return num1/num2

def print_menu():
    print("\n" * 5)
    print('-' * 20)
    print("   MENU   ")
    print("1 - Sum")
    print("2 - Sub")
    print("3 - Mul")
    print("4 - Div")
    print("x - Exit")
 


print('*' * 20)
print(" Welcome to my Calc")
print("*" * 20)

num1 = input("Please provide num1: ")
num2 = input("Please provide num2: ") 

f_num1 = float(num1)
f_num2 = float(num2)



opc = ' '
while( opc != "x"):
    print_menu()
    opc = input("Select an option")
        
    if(opc == "1"):
        res = perform_sum(f_num1, f_num2)
        print("Result: " + str(res))

    elif (opc == "4"):
        res = perform_div(f_num1, f_num2)
        print("Result: " + str(res))

print("")
print("Thank you, later ")

    