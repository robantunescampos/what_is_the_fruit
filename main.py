from functions.choose_fruit import choose_fruit

print('Em qual fruta estou pensando?')

fruit = choose_fruit()

user = input('Em qual fruta estou pensando? ')

while (user != fruit):
    user = input('Vamos tentar novamente: ')

print('Parabéns você acertou, eu estava pensando em ' + fruit)