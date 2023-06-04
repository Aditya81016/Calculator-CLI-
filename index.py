# index.py

import functions as fn

takeInput = True

while (takeInput):

    equation = input("Enter the equation: ")
    equation = fn.format(equation)
    validate = fn.validate(equation)

    if (validate == True):
        takeInput = False

    else:
        error_pointer = ""
        for i in range(validate[0]):
            error_pointer += " "
        error_pointer += "^"

        print('invalid equation, try again')
        print(equation)
        print(error_pointer)
        print("Error:", validate[1])

print("Output:", fn.evaluate(equation))
