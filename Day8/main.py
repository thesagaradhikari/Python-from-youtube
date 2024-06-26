#This is the calculator to do some calculations 
print("write the two numbers to do calculations")
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
choice = int(input("enter the choice:"))
if choice == 1:
    print("The sum of the two numbers is: ",num1+num2)
elif choice == 2:
    print("The difference of the two numbers is: ",num1-num2)
elif choice == 3:
    print("The multiplication of the two numbers is: ",num1*num2)
elif choice == 4:
    print("The division of the two numbers is: ",num1/num2)        
