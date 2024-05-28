#PROCEDURES
#define the functions needed : sum,div,mul,and sub.
#allow the user to choose the operator
# ask input of numbers from the user.
# call the function to do the computation
#while loop to continue the program until the user wants to exit.

def add(a,b):
    answer = a + b
    print(str(a) , "+" , str(b) , "=" , str(answer))

def sub(a,b):
    answer = a - b
    print(str(a) , "-" , str(b) , "=" , str(answer))

def mul(a,b):
    answer = a * b
    print(str(a) , "*" , str(b) , "=" , str(answer))
          
def div(a,b):
    answer = a / b
    print(str(a) , "/" , str(b) , "=" , str(answer))

while True:
 print(" A. Addition")
 print(" B. Subtraction")
 print(" C. Multiplication")
 print(" D. Division")
 print(" E. Exit")

 operator = input("Which operator do you want to use ?")

 a = int(input("Enter first integer:"))
 b = int(input("Enter second integer:"))

 if operator == "a" or operator == "A": 
    add(a,b)
 elif operator == "b" or operator == "B":
    sub(a,b)
 elif operator == "c" or operator == "C":
    mul(a,b)
 elif operator == "d" or operator == "D":
    div(a,b)
 else:
    print("Already Exitted!")
    quit()

