score = 0

print('В каком году началась Вторая мировая война?')
print('а) 1914')
print('б) 1939')
print('в) 1937')
print('г) 1941')

answer = input('Выберите ответ: ')

if answer == 'б':
    print('Правильно!')
    score += 1
else:
    print('Неправильно!')
