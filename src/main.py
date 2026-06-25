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
    if second_number == '0':
        return 'NOT DEFIEND'
    if operator == '+':
        result = float(first_number) + float(second_number)
    elif operator == '-':
        result = float(first_number) - float(second_number)
    elif operator == '*':
        result = float(first_number) * float(second_number)
    elif operator == '/':
        if int(second_number) == 0:
            return 'NOT DEFIEND '
        result = float(first_number) / float(second_number)
    

    if result.is_integer():
        return str(int(result))
    else:
        return str(result)

if __name__ == '__main__':
    first_number = get_number()
    print(first_number,' ')
    operator = get_operation()
    print(first_number, operator)
    second_number = get_number()
    result = calculate(first_number, operator, second_number)
    print(first_number, operator, second_number, ' = ', result )