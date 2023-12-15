import random

def choose_fruit():
    fruits = ['Banana', 'Maçã', 'Manga', 'Morango', 'Laranja']
    # print(fruits)
    random.shuffle(fruits)
    # print(fruits)
    fruit = random.choice(fruits)
    # print(fruit)
    return fruit

# choose_fruit(fruits=fruits)