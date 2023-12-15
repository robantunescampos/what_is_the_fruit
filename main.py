from functions.choose_fruit import choose_fruit

fruit = choose_fruit()

chances = 3

while (chances > 0):
    user = input('Em que fruta estou pensando? ')

    if (user == fruit):
        print('Parabéns você acertou, eu estava pensando em ' + fruit)
        break

    chances-=1

if (chances == 0):
    print('suas chances acabaram.')