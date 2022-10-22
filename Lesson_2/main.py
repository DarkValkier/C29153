a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

while True:
    print('MENU')
    print('1) Деление')
    print('2) Замена чисел')
    print('0) Выход')

    action = input('Укажите номер действия:')

    if action == '0':
        break
    elif action == '1':
        if b == 0:
            print('Делить на ноль нельзя!')
        else:
            print(f'{a} / {b} = {a/b}')
    elif action == '2':
        a = int(input('Введите первое число:'))
        b = int(input('Введите второе число:'))