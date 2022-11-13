a = 5
b = 0

try:
    print(с + a/b)
except ZeroDivisionError:
    print('На ноль делить нельзя!')
except Exception as error:
    print(f'Что-то пошло не так: {error}')
else:
    print('Ошибка не выдалась')