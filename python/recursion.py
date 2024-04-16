def calculator(operation,n1,n2):
    return operation(n1,n2)

n1= float(input("Enter two numbers: "))
n2= float(input("Enter two numbers: "))

result_add = calculator(lambda n1,n2: n1+n2, n1,n2)
print ("Result of addition is:",result_add)

result_sub = calculator(lambda n1,n2: n1-n2, n1,n2)
print ("Result of subtraction is:",result_sub)

result_div = calculator(lambda n1,n2: n1/n2, n1,n2)
print ("Result of Division is:",result_div)

result_multiply = calculator(lambda n1,n2: n1*n2, n1,n2)
print ("Result of Multiplication is:",result_multiply)