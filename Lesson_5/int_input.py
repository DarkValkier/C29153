def input_int(message):
    while True:
        try:
            result = float(input(message))
        except ValueError:
            print('Некорректное значение!')
        else:
            return result


a = input_int('a=')
b = input_int('b=')