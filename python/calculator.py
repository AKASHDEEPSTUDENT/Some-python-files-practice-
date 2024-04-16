def calculator(operation, n1,n2):
    return operation (n1,n2)

n1= float(input("Enter 1st number:"))
n2= float(input("Enter 2nd number:"))

command = input("Enter the operation name:")

if (command == "Addition"):
    result_add=calculator(lambda n1,n2: n1+n2, n1,n2)
    print ("Result of addition is: ", result_add)
elif(command == "Subtraction"):
    result_sub=calculator(lambda n1,n2: n1-n2, n1,n2)
    print_sub=calculator(lambda n1,n2: n1-n2, n1,n2)
    
else:
    print("Number is not valid")