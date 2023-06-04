# functions.py

watch_global_process = False

# formats a string
def format(string):

    watch_process = True
    if (not watch_global_process):
        watch_process = False

    # removes all the whitespace from a string
    i = 0
    while (string.find(' ') >= 0):
        if (string[i] == ' '):

            # skiping the character with whitespace
            string = string[:i] + string[i+1:]
            i -= 1
            if watch_process:
                print(string)

        i += 1
    
    i = 0
    while(i < len(string)-1):

        # checks if there a digit right next to something which isnt
        if (string[i].isdigit() and not string[i+1].isdigit()):

            # and adds space between them
            string = string[:i+1] + " " + string[i+1:]
            i += 1
            if watch_process:
                print(string)

        # checks if there a non digit right next to something which is a digit
        elif (not string[i].isdigit() and string[i+1].isdigit()):
            # and adds space between them
            string = string[:i+1] + " " + string[i+1:]
            i += 1
            if watch_process:
                print(string)
        # checks if there a non digit right next to something which is a non digit
        elif (not string[i].isdigit() and not string[i+1].isdigit()):
            # and adds space between them
            string = string[:i+1] + " " + string[i+1:]
            i += 1
            if watch_process:
                print(string)


        i += 1

    if string[0] != "(":
        string = "( " + string + " )"

    while(string.find(". 0") >= 0):
        string = string.replace(". 0", "")
        string = format(string)


    return string

# verifies whether a given string is 
# valid as a equation or not
def validate(string):
    valid = True
    open_brackets = 0
    close_brackets = 0
    error_index = 0
    error_message = ''
    
    for i in range(len(string)):
        char = string[i]
        error_index = i

        if ((not char.isdigit()) and char != "(" and char != ")" and char != "/" and char != "*" and char != "+" and char != "-" and char != " " ):
            error_message = "unexpected character"
            return [error_index, error_message]

        # validates brackets placing
        if (char == '('):
            open_brackets += 1
        elif (char == ')'):
            close_brackets += 1

        if (close_brackets - open_brackets > 0):
            error_message = 'extra closing bracket'
            return [error_index, error_message]


    
    if (open_brackets - close_brackets != 0):
        error_index += 1
        error_message = 'missing closing bracket'
        return [error_index, error_message]

    return True

# evaluates the given string
def evaluate(string):
    i = 0
    close_brackets = 0
    print(string)

    while (string.find(" ") >= 0 and i < len(string)):
        char = string[i]

        if char == "(":
            bracket_index = i 
        
        if char == ")":
            value = evaluate(string[bracket_index+2 : i])
            string = string[:bracket_index] + value + string[i+1:]
            string = evaluate(string)
            
        i += 1
    
    while string.find('/') >= 0:
        arr = string.split(" ")
        x = arr.index('/')
        arr[x-1] = float(arr[x-1]) / float(arr[x+1])
        arr[x] = ""
        arr[x+1] = ""
        string = arr_to_string(arr)
    
    while string.find('*') >= 0:
        arr = string.split(" ")
        x = arr.index('*')
        arr[x-1] = float(arr[x-1]) * float(arr[x+1])
        arr[x] = ""
        arr[x+1] = ""
        string = arr_to_string(arr)
     
    while string.find('+') >= 0:
        arr = string.split(" ")
        x = arr.index('+')
        arr[x-1] = float(arr[x-1]) + float(arr[x+1])
        arr[x] = ""
        arr[x+1] = ""
        string = arr_to_string(arr)
    
    while string.find('-') >= 0:
        arr = string.split(" ")
        x = arr.index('-')
        arr[x-1] = float(arr[x-1]) - float(arr[x+1])
        arr[x] = ""
        arr[x+1] = ""
        string = arr_to_string(arr)
    
       
    return string 

# converts array into string
def arr_to_string(arr) :
    string = ""
    for item in arr:
        string += str(item)

    string = format(string)
    return string
    
