#This is a basic calculator , make it advanced next time
memory_answer = None
VAR_1 = ("Do you want to continue with the old calculation {yes / no}  ").lower()

while True:
    print("---new_calculation---")
    if memory_answer is not None:
        print(memory_answer)
    user_choice = input("enter start to start calculation or exit to exit: ").lower()
    
    if user_choice == "exit":
        print("goodbye")
        break  
    elif user_choice == "start":
        if memory_answer is not None:
            USER_RESPONSE = input(VAR_1).lower()
            if USER_RESPONSE == "no":
                memory_answer = None
                print ("Memory cleared")
                continue
            elif USER_RESPONSE == "yes":
                pass
        try:
            if memory_answer is not None:
                var_1 = memory_answer
                print(var_1)
            else:
                var_1 = float(input("Enter a number  "))
                
            basic_operator = input("enter any of these operators:+ , - , * , /,^.   ")
            var_2 = float(input("Enter a second number  "))
       
    
            if basic_operator == "+":
                memory_answer = (var_1 + var_2)
                print(memory_answer)  
            elif basic_operator == "-": 
                memory_answer = (var_1 - var_2)
                print(memory_answer)
            elif basic_operator == "*":
                memory_answer = (var_1 * var_2)
                print(memory_answer)
            elif basic_operator == "/":
                if var_2 == 0:
                    print("You can\'t divide with 0!")
                else:
                    memory_answer = (var_1/var_2)
                    print(memory_answer)
            elif basic_operator == "^":
                
                memory_answer = (pow(var_1, var_2))
                
                print(memory_answer)
            else:
                print("Invalid operator")
        except:
            print("enter valid numbers only!")
