print("Created by Nandini Sangal")
print("Welcome to the basic calculator for two numbers")
user_input_a= float(input("Enter first number: "))
user_input_b= float(input("Enter second number: "))
user_computation=input("Which operation does you want to perform select (1,2,3,4,5,6)\n1 for ARITHMETIC[Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus (%), Exponentiation (**), Floor Division (//).]\n2 for COMPARISON[Equal to (==), Not equal to (!=), Greater than (>), Less than (<), Greater than or equal to (>=), Less than or equal to (<=)]\n3 for LOGICAL[AND('and'), OR('or'), NOT('not')]\n4 for BITWISE[Bitwise AND (&), Bitwise OR (|), Bitwise XOR (^), Bitwise NOT (~), Left shift (<<), Right shift (>>)]\n5 for ASSIGNMENT[Assignment (=), Addition assignment (+=), Subtraction assignment (-=), Multiplication assignment (*=), Division assignment (/=), Modulus assignment (%=), Exponentiation assignment (**=), Floor division assignment (//=)\n6 for IDENTITY['is': Returns 'True' if both variables point to the same object.\n\t\t\t\t'is not': Returns 'True' if both variables do not point to the same object.] ")
if user_computation == '1': #Arithmetic operation
    user_operation =input("Select an arithmetic operation[+,-,*,/,%,**,//]")
    if user_operation == '+':
        user_output = user_input_a + user_input_b
    elif user_operation == '-':
        user_output = user_input_a - user_input_b
    elif user_operation == '*':
        user_output = user_input_a * user_input_b
    elif user_operation == '/':
        if user_input_b != 0:
            user_output = user_input_a / user_input_b
        else:
            print("Error: Cannot divide by zero.")
    elif user_operation == '%':
        user_output = user_input_a % user_input_b
    elif user_operation == '**':  
        user_output = user_input_a ** user_input_b
    elif user_operation == '//': 
        user_output = user_input_a ** user_input_b
    else:
        print("Error: Invalid Arithmetic operation selected try again.")
elif user_computation == '2': #Comparison operation
    user_operation =input("Select an comparison operation[==,!=,>,<,>=,<=]")
    if user_operation == '==':
        user_output = user_input_a == user_input_b
    elif user_operation == '!=':
        user_output = user_input_a != user_input_b
    elif user_operation == '>':
        user_output = user_input_a > user_input_b
    elif user_operation == '<':
        user_output = user_input_a < user_input_b
    elif user_operation == '>=':
        user_output = user_input_a >= user_input_b
    elif user_operation == '<=':
        user_output = user_input_a <= user_input_b
    else:
        print("Error: Invalid Comparison operation selected try again.")
elif user_computation == '3': # Logical Operations
    user_operation = input("Select a logical operation (and, or, not): ")
    if user_operation == 'and':
        user_output = user_input_a and user_input_b
    elif user_operation == 'or':
        user_output = user_input_a or user_input_b
    elif user_operation == 'not':
        user_input =input("Select one number(a,b):")
        if user_input== 'a':
            user_output = not user_input_a
        elif user_input== 'b':
            user_output = not user_input_b
        else:
            print("Error: Invalid input for 'not' operation. Try again.")
            exit()
    else:
        print("Error: Invalid logical operation selected. Try again.")
        exit()
elif user_computation == '4':  # Bitwise Operations
    user_operation = input("Select a bitwise operation [&, |, ^, ~, <<, >>]: ")
    if user_operation == '&':
        user_output = int(user_input_a) & int(user_input_b)
    elif user_operation == '|':
        user_output = int(user_input_a) | int(user_input_b)
    elif user_operation == '^':
        user_output = int(user_input_a) ^ int(user_input_b)
    elif user_operation == '~':
        user_input =input("Select one number(a,b):")
        if user_input== 'a':
            user_output = ~int(user_input_a)
        elif user_input== 'b':
            user_output = ~int(user_input_b)
        else:
            print("Error: Invalid input for '~' operation. Try again.")
            exit()
    elif user_operation == '<<':
        user_output = int(user_input_a) << int(user_input_b)
    elif user_operation == '>>':
        user_output = int(user_input_a) >> int(user_input_b)
    else:
        print("Error: Invalid Bitwise operation selected. Try again.")
        exit()
elif user_computation == '5':  # Assignment Operations
    user_operation = input("Select an assignment operation [=, +=, -=, *=, /=, %=, **=, //=]: ")
    if user_operation == '=':
        user_output = user_input_a
    elif user_operation == '+=':
        user_input_a += user_input_b
        user_output = user_input_a
    elif user_operation == '-=':
        user_input_a -= user_input_b
        user_output = user_input_a
    elif user_operation == '*=':
        user_input_a *= user_input_b
        user_output = user_input_a
    elif user_operation == '/=':
        if user_input_b != 0:
            user_input_a /= user_input_b
            user_output = user_input_a
        else:
            print("Error: Cannot divide by zero.")
            exit()
    elif user_operation == '%=':
        user_input_a %= user_input_b
        user_output = user_input_a
    elif user_operation == '**=':
        user_input_a **= user_input_b
        user_output = user_input_a
    elif user_operation == '//=':
        user_input_a //= user_input_b
        user_output = user_input_a
    else:
        print("Error: Invalid Assignment operation selected. Try again.")
        exit()

elif user_computation == '6':  # Identity Operations
    user_operation = input("Select an identity operation ['is', 'is not']: ")
    if user_operation == 'is':
        user_output = user_input_a is user_input_b
    elif user_operation == 'is not':
        user_output = user_input_a is not user_input_b
    else:
        print("Error: Invalid Identity operation selected. Try again.")
        exit()

# Display the result
print("Result:", user_output)



       
        
        
                            
    
        
        
    
    
    






