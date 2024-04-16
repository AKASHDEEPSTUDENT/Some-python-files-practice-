#this is the simplest calculator 
num1= float(input("Enter number 1:"))
num2= float(input("Enter number 2:"))

print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for Division\nPress 5 for modulus")

choice= int(input("Enter your choice from 1-5"))

if choice ==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
elif choice==5:
    print(num1%num2)
else:
    print("Invalid entry")