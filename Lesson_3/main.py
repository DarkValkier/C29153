from character import Character

player1 = Character(name='Vasya', damage=10)
player2 = Character(name='Petya', damage=8)

print(player1, '\n')
print(player2, '\n')


while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(player1, '\n')
    print(player2, '\n')