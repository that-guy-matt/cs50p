user_input = input("Input an arithmetic calculation: ").split()

if (user_input[1] == '+'):
    print(float(user_input[0]) + float(user_input[2]))
elif (user_input[1] == '-'):
    print(float(user_input[0]) - float(user_input[2]))
elif (user_input[1] == '*'):
    print(float(user_input[0]) * float(user_input[2]))
elif (user_input[1] == '/'):
    print(float(user_input[0]) / float(user_input[2]))