def get_number():
    while 1:
        number = input('Enter a number: ')
        try:
            number = int(number)
            return number
        except:
            print('Wrong input!')


def get_operation():
    while 1:
        ALLOWED_OPERATIONS = ['+', '-', '/', '*']
        operation = input('Enter operation: ')
        if operation in ALLOWED_OPERATIONS:
            return operation
        else:
            print('Wrong input!')


def calculate(first_number, operator, second_number):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        return first_number / second_number
    

if __name__ == '__main__':
    first_number = get_number()
    print(first_number,' ')
    operator = get_operation()
    print(first_number, operator)
    second_number = get_number()
    result = calculate(first_number, operator, second_number)
    print(first_number, operator, second_number, ' = ', result )